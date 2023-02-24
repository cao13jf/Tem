## Problem description
When running `main.py` in PyCharm, the function of `Import TF` works fine. However, when the GUI is packaged with `pyinstaller main.spec`, an error was raised as follows:
```text
Traceback (most recent call last):
  File "main.py", line 36, in import_tf
    self.model = tf.keras.Sequential()
  File "tensorflow/python/training/tracking/base.py", line 530, in _method_wrapper
  File "keras/engine/sequential.py", line 107, in __init__
  File "tensorflow/python/training/tracking/base.py", line 530, in _method_wrapper
  File "keras/engine/training.py", line 289, in __init__
  File "tensorflow/python/training/tracking/base.py", line 530, in _method_wrapper
  File "keras/engine/training.py", line 297, in _init_batch_counters
  File "tensorflow/python/ops/variables.py", line 268, in __call__
  File "tensorflow/python/ops/variables.py", line 250, in _variable_v2_call
  File "tensorflow/python/ops/variables.py", line 243, in <lambda>
  File "tensorflow/python/ops/variable_scope.py", line 2662, in default_variable_creator_v2
  File "tensorflow/python/ops/variables.py", line 270, in __call__
  File "tensorflow/python/ops/resource_variable_ops.py", line 1602, in __init__
  File "tensorflow/python/ops/resource_variable_ops.py", line 1756, in _init_from_args
  File "tensorflow/python/ops/resource_variable_ops.py", line 238, in eager_safe_variable_handle
  File "tensorflow/python/ops/resource_variable_ops.py", line 178, in _variable_handle_from_shape_and_dtype
TypeError: Parameter to MergeFrom() must be instance of same class: expected tensorflow.TensorShapeProto got tensorflow.TensorShapeProto.
```
To inspect this error, the software is executed in command line with
```shell
Path2Project/dist/main.app/Contents/MacOS/main
```

The code was tested on MacOS and Linux, both of which raise the same problem.