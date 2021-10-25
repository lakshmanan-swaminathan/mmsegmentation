_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py',
    '../_base_/datasets/stanford.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
norm_cfg = dict(type='BN', requires_grad=True)

model = dict(
    backbone = dict(
        norm_cfg = norm_cfg
        ),
    decode_head=dict(
        norm_cfg = norm_cfg, 
        num_classes=8
        ),
    auxiliary_head=dict(
        norm_cfg = norm_cfg,
        num_classes=8),
    )


runner = dict(max_iters = 1000)
evaluation = dict(interval = 100)
checkpoint_config = dict(interval = 1000)
