_base_ = [
    '../_base_/models/lraspp_m-v3-d8.py', '../_base_/datasets/stanford.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]


norm_cfg = dict(type='BN', eps=0.001, requires_grad=True)

model = dict(
    pretrained='open-mmlab://contrib/mobilenet_v3_large',
    backbone = dict(
        norm_cfg = norm_cfg
        ),
    decode_head=dict(
        norm_cfg = norm_cfg, 
        num_classes=8
        )
    )

runner = dict(type='IterBasedRunner', max_iters=1000)
evaluation = dict(interval = 100)
checkpoint_config = dict(interval = 1000)
