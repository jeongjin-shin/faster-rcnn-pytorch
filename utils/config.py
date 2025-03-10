from pprint import pprint


# Default Configs for training
# NOTE that, config items could be overwriten by passing argument through command line.
# e.g. --voc-data-dir='./data/'

class Config:
    # data
    dataset = 'voc2007' #or coco
    data_dir = '/home/jjshin/invisible-backdoor-object-detection/VOCdevkit/VOC2007'
    min_size = 600  # image resize
    max_size = 1000 # image resize
    num_workers = 8
    test_num_workers = 8

    # sigma for l1_smooth_loss
    rpn_sigma = 3.
    roi_sigma = 1.

    epsilon = 0.05
    stage2 = 0  #0 or 1
    attack_type = 'd'
    target_class = 14
    atk_model = "autoencoder" #unet or autoencoder
    poisoning_rate = 0.3

    # param for ae optimizer
    lr_atk = 1e-5

    # param for optimizer
    # 0.0005 in origin paper but 0.0001 in tf-faster-rcnn
    weight_decay = 0.0005
    lr_decay = 0.1  # 1e-3 -> 1e-4
    lr = 1e-3

    
    # propotion of loss_poison, loss_clean
    alpha = 0.5

    # visualization
    env = 'OMA'  # visdom env
    env2 = f'{env}_loss_clean'
    env3 = f'{env}_loss_poison'
    port = 8097
    plot_every = 100  # vis every N iter

    # preset
    data = 'voc'
    pretrained_model = 'vgg16'

    # training
    epoch = 22

    checkpoint_epoch = 0


    use_adam = False # Use Adam optimizer
    use_chainer = False # try match everything as chainer
    use_drop = False # use dropout in RoIHead
    # debug
    debug_file = '/tmp/debugf'

    test_num = 1000
    # model
    load_path = None
    load_path_atk = None

    caffe_pretrain = False # use caffe pretrained model instead of torchvision
    caffe_pretrain_path = 'checkpoints/vgg16_caffe.pth'

    def _parse(self, kwargs):
        state_dict = self._state_dict()
        for k, v in kwargs.items():
            if k not in state_dict:
                raise ValueError('UnKnown Option: "--%s"' % k)
            setattr(self, k, v)

        print('======user config========')
        pprint(self._state_dict())
        print('==========end============')

    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in Config.__dict__.items() \
                if not k.startswith('_')}


opt = Config()
