python train_cider.py \
    --in-dataset CIFAR-100\
    --id_loc datasets/CIFAR100 \
    --gpu 0 \
    --model resnet34 \
    --loss cider \
    --epochs 500 \
    --proto_m 0.5 \
    --feat_dim 128 \
    --w_dis 2 \
    --batch-size 2 \
    --cosine