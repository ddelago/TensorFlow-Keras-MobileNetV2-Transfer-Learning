import os

num_steps = 1000  # 200000
num_eval_steps = 50
batch_size = 12

# Downloaded from tensorflow model zoo
selected_model = 'ssd_mobilenet_v2_coco_2018_03_29'

# Found in object_detection/samples/config
pipeline_file = 'ssd_mobilenet_v2_coco.config'

# Output trained model directory
model_dir = 'trained_model'

os.system(
  f'''python model_main.py \
  --pipeline_config_path={pipeline_file} \
  --model_dir={model_dir} \
  --alsologtostderr \
  --num_train_steps={num_steps} \
  --num_eval_steps={num_eval_steps}
  '''
)


