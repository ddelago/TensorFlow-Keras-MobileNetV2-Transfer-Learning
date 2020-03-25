import os

# Found in object_detection/samples/config
pipeline_file = 'ssd_mobilenet_v2_coco.config'

# Output trained model directory
out_dir = 'trained_inference_graph'

# Last saved checkpoint in training
checkpoint = 'trained_model/model.ckpt-20000'

os.system(
    f'''python export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path={pipeline_file} \
    --output_directory={out_dir} \
    --trained_checkpoint_prefix={checkpoint}
    '''
)


