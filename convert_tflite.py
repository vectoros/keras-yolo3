from keras.models import load_model
from tensorflow import lite


def keras_to_tflite(input_keras_model_file, output_tflite_file):
    keras_model = load_model(input_keras_model_file)
    input_names = get_input_names(keras_model)
    output_names = get_output_names(keras_model)
    print("input names:", input_names, " shapes:", keras_model.input_shape)
    print("output names:", output_names, " shapes:", keras_model.output_shape)
    converter = lite.TFLiteConverter.from_keras_model_file(model_file=input_keras_model_file,
                                                           input_arrays=input_names,
                                                           output_arrays=output_names)
    model = converter.convert()
    file = open(output_tflite_file, "wb")
    file.write(model)
    print("save tflite file to: ", output_tflite_file)


def get_output_names(keras_model):
    outputs = keras_model.outputs
    output_names = []
    for _output in outputs:
        output_names.append(_output.name[:-2])
    return output_names


def get_input_names(keras_model):
    inputs = keras_model.inputs
    input_names = []
    for _input in inputs:
        input_names.append(_input.name[:-2])
    return input_names



def main():
    keras_model_file = "./model_data/yolov3.h5"
    tflite_model_file = "./model_data/yolov3.tflite"
    keras_to_tflite(keras_model_file, tflite_model_file)


if __name__ == '__main__':
    main()