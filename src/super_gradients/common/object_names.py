class Losses:
    """Static class holding all the supported loss names"""

    CROSS_ENTROPY = "cross_entropy"
    MSE = "mse"
    R_SQUARED_LOSS = "r_squared_loss"
    SHELFNET_OHEM_LOSS = "shelfnet_ohem_loss"
    SHELFNET_SE_LOSS = "shelfnet_se_loss"
    YOLOX_LOSS = "yolox_loss"
    PPYOLOE_LOSS = "ppyoloe_loss"
    YOLOX_FAST_LOSS = "yolox_fast_loss"
    SSD_LOSS = "ssd_loss"
    STDC_LOSS = "stdc_loss"
    BCE_DICE_LOSS = "bce_dice_loss"
    KD_LOSS = "kd_loss"
    DICE_CE_EDGE_LOSS = "dice_ce_edge_loss"
    DEKR_LOSS = "dekr_loss"
    RESCORING_LOSS = "rescoring_loss"


class Metrics:
    """Static class holding all the supported metric names"""

    ACCURACY = "Accuracy"
    TOP5 = "Top5"
    DETECTION_METRICS = "DetectionMetrics"
    DETECTION_METRICS_050_095 = "DetectionMetrics_050_095"
    DETECTION_METRICS_050 = "DetectionMetrics_050"
    DETECTION_METRICS_075 = "DetectionMetrics_075"
    IOU = "IoU"
    BINARY_IOU = "BinaryIOU"
    DICE = "Dice"
    BINARY_DICE = "BinaryDice"
    PIXEL_ACCURACY = "PixelAccuracy"
    POSE_ESTIMATION_METRICS = "PoseEstimationMetrics"


class Transforms:
    """Static class holding all the supported transform names"""

    # From SG
    SegRandomFlip = "SegRandomFlip"
    SegResize = "SegResize"
    SegRescale = "SegRescale"
    SegRandomRescale = "SegRandomRescale"
    SegRandomRotate = "SegRandomRotate"
    SegCropImageAndMask = "SegCropImageAndMask"
    SegRandomGaussianBlur = "SegRandomGaussianBlur"
    SegPadShortToCropSize = "SegPadShortToCropSize"
    SegPadToDivisible = "SegPadToDivisible"
    SegColorJitter = "SegColorJitter"
    DetectionStandardize = "DetectionStandardize"
    DetectionMosaic = "DetectionMosaic"
    DetectionRandomAffine = "DetectionRandomAffine"
    DetectionMixup = "DetectionMixup"
    DetectionHSV = "DetectionHSV"
    DetectionRGB2BGR = "DetectionRGB2BGR"
    DetectionRandomRotate90 = "DetectionRandomRotate90"
    DetectionHorizontalFlip = "DetectionHorizontalFlip"
    DetectionVerticalFlip = "DetectionVerticalFlip"
    DetectionRescale = "DetectionRescale"
    DetectionPadToSize = "DetectionPadToSize"
    DetectionImagePermute = "DetectionImagePermute"
    DetectionPaddedRescale = "DetectionPaddedRescale"
    DetectionTargetsFormatTransform = "DetectionTargetsFormatTransform"
    DetectionNormalize = "DetectionNormalize"
    #
    RandomResizedCropAndInterpolation = "RandomResizedCropAndInterpolation"
    RandAugmentTransform = "RandAugmentTransform"
    Lighting = "Lighting"
    RandomErase = "RandomErase"
    Standardize = "Standardize"

    # From torch
    Compose = "Compose"
    ToTensor = "ToTensor"
    PILToTensor = "PILToTensor"
    ConvertImageDtype = "ConvertImageDtype"
    ToPILImage = "ToPILImage"
    Normalize = "Normalize"
    Resize = "Resize"
    CenterCrop = "CenterCrop"
    Pad = "Pad"
    Lambda = "Lambda"
    RandomApply = "RandomApply"
    RandomChoice = "RandomChoice"
    RandomOrder = "RandomOrder"
    RandomCrop = "RandomCrop"
    RandomHorizontalFlip = "RandomHorizontalFlip"
    RandomVerticalFlip = "RandomVerticalFlip"
    RandomResizedCrop = "RandomResizedCrop"
    FiveCrop = "FiveCrop"
    TenCrop = "TenCrop"
    LinearTransformation = "LinearTransformation"
    ColorJitter = "ColorJitter"
    RandomRotation = "RandomRotation"
    RandomAffine = "RandomAffine"
    Grayscale = "Grayscale"
    RandomGrayscale = "RandomGrayscale"
    RandomPerspective = "RandomPerspective"
    RandomErasing = "RandomErasing"
    GaussianBlur = "GaussianBlur"
    InterpolationMode = "InterpolationMode"
    RandomInvert = "RandomInvert"
    RandomPosterize = "RandomPosterize"
    RandomSolarize = "RandomSolarize"
    RandomAdjustSharpness = "RandomAdjustSharpness"
    RandomAutocontrast = "RandomAutocontrast"
    RandomEqualize = "RandomEqualize"

    # Keypoints
    KeypointsRandomAffineTransform = "KeypointsRandomAffineTransform"
    KeypointsImageNormalize = "KeypointsImageNormalize"
    KeypointsImageStandardize = "KeypointsImageStandardize"
    KeypointsImageToTensor = "KeypointsImageToTensor"
    KeypointTransform = "KeypointTransform"
    KeypointsPadIfNeeded = "KeypointsPadIfNeeded"
    KeypointsLongestMaxSize = "KeypointsLongestMaxSize"
    KeypointsRandomVerticalFlip = "KeypointsRandomVerticalFlip"
    KeypointsRandomHorizontalFlip = "KeypointsRandomHorizontalFlip"


class Optimizers:
    """Static class holding all the supported optimizer names"""

    SGD = "SGD"
    ADAM = "Adam"
    ADAMW = "AdamW"
    RMS_PROP = "RMSprop"
    RMS_PROP_TF = "RMSpropTF"
    LAMB = "Lamb"
    LION = "Lion"


class Callbacks:
    """Static class holding all the supported callback names"""

    DECI_LAB_UPLOAD = "DeciLabUploadCallback"
    LR_CALLBACK_BASE = "LRCallbackBase"
    LR_SCHEDULER = "LRSchedulerCallback"
    METRICS_UPDATE = "MetricsUpdateCallback"
    MODEL_CONVERSION_CHECK = "ModelConversionCheckCallback"
    EARLY_STOP = "EarlyStop"
    DETECTION_MULTISCALE_PREPREDICTION = "DetectionMultiscalePrePredictionCallback"
    YOLOX_TRAINING_STAGE_SWITCH = "YoloXTrainingStageSwitchCallback"
    PPYOLOE_TRAINING_STAGE_SWITCH = "PPYoloETrainingStageSwitchCallback"
    DETECTION_VISUALIZATION_CALLBACK = "DetectionVisualizationCallback"
    DEKR_VISUALIZATION = "DEKRVisualizationCallback"
    ROBOFLOW_RESULT_CALLBACK = "RoboflowResultCallback"


class LRSchedulers:
    """Static class to hold all the supported LR Scheduler names"""

    STEP = "step"
    POLY = "poly"
    COSINE = "cosine"
    EXP = "exp"
    FUNCTION = "function"


class LRWarmups:
    """Static class to hold all the supported LR Warmup names"""

    LINEAR_STEP = "linear_step"
    LINEAR_EPOCH_STEP = "linear_epoch_step"
    LINEAR_BATCH_STEP = "linear_batch_step"


class Samplers:
    """Static class to hold all the supported Samplers names"""

    REPEAT_AUG = "RepeatAugSampler"
    DISTRIBUTED = "DistributedSampler"
    SEQUENTIAL = "SequentialSampler"
    SUBSET_RANDOM = "SubsetRandomSampler"
    RANDOM = "RandomSampler"
    WEIGHTED_RANDOM = "WeightedRandomSampler"


class ContextModules:
    """Static class to hold all the segmentation context module names"""

    ASPP = "ASPP"
    SPPM = "SPPM"


class Models:
    """Static class to hold all the available model names"""

    RESNET18 = "resnet18"
    RESNET34 = "resnet34"
    RESNET50_3343 = "resnet50_3343"
    RESNET50 = "resnet50"
    RESNET101 = "resnet101"
    RESNET152 = "resnet152"
    RESNET18_CIFAR = "resnet18_cifar"
    CUSTOM_RESNET = "custom_resnet"
    CUSTOM_RESNET50 = "custom_resnet50"
    CUSTOM_RESNET_CIFAR = "custom_resnet_cifar"
    CUSTOM_RESNET50_CIFAR = "custom_resnet50_cifar"
    MOBILENET_V2 = "mobilenet_v2"
    MOBILE_NET_V2_135 = "mobile_net_v2_135"
    CUSTOM_MOBILENET_V2 = "custom_mobilenet_v2"
    MOBILENET_V3_LARGE = "mobilenet_v3_large"
    MOBILENET_V3_SMALL = "mobilenet_v3_small"
    MOBILENET_V3_CUSTOM = "mobilenet_v3_custom"
    CUSTOM_DENSENET = "custom_densenet"
    DENSENET121 = "densenet121"
    DENSENET161 = "densenet161"
    DENSENET169 = "densenet169"
    DENSENET201 = "densenet201"
    SHELFNET18_LW = "shelfnet18_lw"
    SHELFNET34_LW = "shelfnet34_lw"
    SHELFNET50_3343 = "shelfnet50_3343"
    SHELFNET50 = "shelfnet50"
    SHELFNET101 = "shelfnet101"
    SHUFFLENET_V2_X0_5 = "shufflenet_v2_x0_5"
    SHUFFLENET_V2_X1_0 = "shufflenet_v2_x1_0"
    SHUFFLENET_V2_X1_5 = "shufflenet_v2_x1_5"
    SHUFFLENET_V2_X2_0 = "shufflenet_v2_x2_0"
    SHUFFLENET_V2_CUSTOM5 = "shufflenet_v2_custom5"
    DARKNET53 = "darknet53"
    CSP_DARKNET53 = "csp_darknet53"
    RESNEXT50 = "resnext50"
    RESNEXT101 = "resnext101"
    GOOGLENET_V1 = "googlenet_v1"
    EFFICIENTNET_B0 = "efficientnet_b0"
    EFFICIENTNET_B1 = "efficientnet_b1"
    EFFICIENTNET_B2 = "efficientnet_b2"
    EFFICIENTNET_B3 = "efficientnet_b3"
    EFFICIENTNET_B4 = "efficientnet_b4"
    EFFICIENTNET_B5 = "efficientnet_b5"
    EFFICIENTNET_B6 = "efficientnet_b6"
    EFFICIENTNET_B7 = "efficientnet_b7"
    EFFICIENTNET_B8 = "efficientnet_b8"
    EFFICIENTNET_L2 = "efficientnet_l2"
    CUSTOMIZEDEFFICIENTNET = "CustomizedEfficientnet"
    REGNETY200 = "regnetY200"
    REGNETY400 = "regnetY400"
    REGNETY600 = "regnetY600"
    REGNETY800 = "regnetY800"
    CUSTOM_REGNET = "custom_regnet"
    CUSTOM_ANYNET = "custom_anynet"
    NAS_REGNET = "nas_regnet"
    YOLOX_N = "yolox_n"
    YOLOX_T = "yolox_t"
    YOLOX_S = "yolox_s"
    YOLOX_M = "yolox_m"
    YOLOX_L = "yolox_l"
    YOLOX_X = "yolox_x"
    CUSTOM_YOLO_X = "custom_yolox"
    SSD_MOBILENET_V1 = "ssd_mobilenet_v1"
    SSD_LITE_MOBILENET_V2 = "ssd_lite_mobilenet_v2"
    REPVGG_A0 = "repvgg_a0"
    REPVGG_A1 = "repvgg_a1"
    REPVGG_A2 = "repvgg_a2"
    REPVGG_B0 = "repvgg_b0"
    REPVGG_B1 = "repvgg_b1"
    REPVGG_B2 = "repvgg_b2"
    REPVGG_B3 = "repvgg_b3"
    REPVGG_D2SE = "repvgg_d2se"
    REPVGG_CUSTOM = "repvgg_custom"
    DDRNET_23 = "ddrnet_23"
    DDRNET_23_SLIM = "ddrnet_23_slim"
    DDRNET_39 = "ddrnet_39"
    CUSTOM_DDRNET_23 = "custom_ddrnet_23"
    STDC1_CLASSIFICATION = "stdc1_classification"
    STDC2_CLASSIFICATION = "stdc2_classification"
    STDC1_SEG = "stdc1_seg"
    STDC1_SEG50 = "stdc1_seg50"
    STDC1_SEG75 = "stdc1_seg75"
    STDC2_SEG = "stdc2_seg"
    STDC2_SEG50 = "stdc2_seg50"
    STDC2_SEG75 = "stdc2_seg75"
    REGSEG48 = "regseg48"
    KD_MODULE = "kd_module"
    VIT_BASE = "vit_base"
    VIT_LARGE = "vit_large"
    VIT_HUGE = "vit_huge"
    BEIT_BASE_PATCH16_224 = "beit_base_patch16_224"
    BEIT_LARGE_PATCH16_224 = "beit_large_patch16_224"
    PP_LITE_T_SEG = "pp_lite_t_seg"
    PP_LITE_T_SEG50 = "pp_lite_t_seg50"
    PP_LITE_T_SEG75 = "pp_lite_t_seg75"
    PP_LITE_B_SEG = "pp_lite_b_seg"
    PP_LITE_B_SEG50 = "pp_lite_b_seg50"
    PP_LITE_B_SEG75 = "pp_lite_b_seg75"
    UNET_CUSTOM = "unet_custom"
    UNET_CUSTOM_CLS = "unet_custom_cls"
    UNET = "unet"
    STDC_CUSTOM = "stdc_custom"
    STDC_CUSTOM_CLS = "stdc_custom_cls"
    PP_YOLOE_S = "ppyoloe_s"
    PP_YOLOE_M = "ppyoloe_m"
    PP_YOLOE_L = "ppyoloe_l"
    PP_YOLOE_X = "ppyoloe_x"
    SEGFORMER_B0 = "segformer_b0"
    SEGFORMER_B1 = "segformer_b1"
    SEGFORMER_B2 = "segformer_b2"
    SEGFORMER_B3 = "segformer_b3"
    SEGFORMER_B4 = "segformer_b4"
    SEGFORMER_B5 = "segformer_b5"

    DEKR_CUSTOM = "dekr_custom"
    DEKR_W32_NO_DC = "dekr_w32_no_dc"
    YOLO_NAS_S = "yolo_nas_s"
    YOLO_NAS_M = "yolo_nas_m"
    YOLO_NAS_L = "yolo_nas_l"
    POSE_RESCORING = "pose_rescoring_custom"
    POSE_RESCORING_COCO = "pose_rescoring_coco"


class ConcatenatedTensorFormats:
    XYXY_LABEL = "XYXY_LABEL"
    XYWH_LABEL = "XYWH_LABEL"
    CXCYWH_LABEL = "CXCYWH_LABEL"
    LABEL_XYXY = "LABEL_XYXY"
    LABEL_XYWH = "LABEL_XYWH"
    LABEL_CXCYWH = "LABEL_CXCYWH"
    NORMALIZED_XYXY_LABEL = "NORMALIZED_XYXY_LABEL"
    NORMALIZED_XYWH_LABEL = "NORMALIZED_XYWH_LABEL"
    NORMALIZED_CXCYWH_LABEL = "NORMALIZED_CXCYWH_LABEL"
    LABEL_NORMALIZED_XYXY = "LABEL_NORMALIZED_XYXY"
    LABEL_NORMALIZED_XYWH = "LABEL_NORMALIZED_XYWH"
    LABEL_NORMALIZED_CXCYWH = "LABEL_NORMALIZED_CXCYWH"


class Dataloaders:
    COCO2017_TRAIN = "coco2017_train"
    COCO2017_VAL = "coco2017_val"
    COCO2017_TRAIN_YOLOX = "coco2017_train_yolox"
    COCO2017_VAL_YOLOX = "coco2017_val_yolox"
    COCO2017_TRAIN_YOLO_NAS = "coco2017_train_yolo_nas"
    COCO2017_VAL_YOLO_NAS = "coco2017_val_yolo_nas"
    COCO2017_TRAIN_PPYOLOE = "coco2017_train_ppyoloe"
    COCO2017_VAL_PPYOLOE = "coco2017_val_ppyoloe"
    COCO2017_TRAIN_SSD_LITE_MOBILENET_V2 = "coco2017_train_ssd_lite_mobilenet_v2"
    COCO2017_VAL_SSD_LITE_MOBILENET_V2 = "coco2017_val_ssd_lite_mobilenet_v2"
    COCO2017_POSE_TRAIN = "coco2017_pose_train"
    COCO2017_POSE_VAL = "coco2017_pose_val"
    COCO_DETECTION_YOLO_FORMAT_TRAIN = "coco_detection_yolo_format_train"
    COCO_DETECTION_YOLO_FORMAT_VAL = "coco_detection_yolo_format_val"
    COCO2017_RESCORING_TRAIN = "coco2017_rescoring_train"
    COCO2017_RESCORING_VAL = "coco2017_rescoring_val"
    IMAGENET_TRAIN = "imagenet_train"
    IMAGENET_VAL = "imagenet_val"
    IMAGENET_EFFICIENTNET_TRAIN = "imagenet_efficientnet_train"
    IMAGENET_EFFICIENTNET_VAL = "imagenet_efficientnet_val"
    IMAGENET_MOBILENETV2_TRAIN = "imagenet_mobilenetv2_train"
    IMAGENET_MOBILENETV2_VAL = "imagenet_mobilenetv2_val"
    IMAGENET_MOBILENETV3_TRAIN = "imagenet_mobilenetv3_train"
    IMAGENET_MOBILENETV3_VAL = "imagenet_mobilenetv3_val"
    IMAGENET_REGNETY_TRAIN = "imagenet_regnetY_train"
    IMAGENET_REGNETY_VAL = "imagenet_regnetY_val"
    IMAGENET_RESNET50_TRAIN = "imagenet_resnet50_train"
    IMAGENET_RESNET50_VAL = "imagenet_resnet50_val"
    IMAGENET_RESNET50_KD_TRAIN = "imagenet_resnet50_kd_train"
    IMAGENET_RESNET50_KD_VAL = "imagenet_resnet50_kd_val"
    IMAGENET_VIT_BASE_TRAIN = "imagenet_vit_base_train"
    IMAGENET_VIT_BASE_VAL = "imagenet_vit_base_val"
    TINY_IMAGENET_TRAIN = "tiny_imagenet_train"
    TINY_IMAGENET_VAL = "tiny_imagenet_val"
    CIFAR10_TRAIN = "cifar10_train"
    CIFAR10_VAL = "cifar10_val"
    CIFAR100_TRAIN = "cifar100_train"
    CIFAR100_VAL = "cifar100_val"
    CITYSCAPES_TRAIN = "cityscapes_train"
    CITYSCAPES_VAL = "cityscapes_val"
    CITYSCAPES_STDC_SEG50_TRAIN = "cityscapes_stdc_seg50_train"
    CITYSCAPES_STDC_SEG50_VAL = "cityscapes_stdc_seg50_val"
    CITYSCAPES_STDC_SEG75_TRAIN = "cityscapes_stdc_seg75_train"
    CITYSCAPES_STDC_SEG75_VAL = "cityscapes_stdc_seg75_val"
    CITYSCAPES_REGSEG48_TRAIN = "cityscapes_regseg48_train"
    CITYSCAPES_REGSEG48_VAL = "cityscapes_regseg48_val"
    CITYSCAPES_DDRNET_TRAIN = "cityscapes_ddrnet_train"
    CITYSCAPES_DDRNET_VAL = "cityscapes_ddrnet_val"
    COCO_SEGMENTATION_TRAIN = "coco_segmentation_train"
    COCO_SEGMENTATION_VAL = "coco_segmentation_val"
    MAPILLARY_TRAIN = "mapillary_train"
    MAPILLARY_VAL = "mapillary_val"
    PASCAL_AUG_SEGMENTATION_TRAIN = "pascal_aug_segmentation_train"
    PASCAL_AUG_SEGMENTATION_VAL = "pascal_aug_segmentation_val"
    PASCAL_VOC_SEGMENTATION_TRAIN = "pascal_voc_segmentation_train"
    PASCAL_VOC_SEGMENTATION_VAL = "pascal_voc_segmentation_val"
    SUPERVISELY_PERSONS_TRAIN = "supervisely_persons_train"
    SUPERVISELY_PERSONS_VAL = "supervisely_persons_val"
    PASCAL_VOC_DETECTION_TRAIN = "pascal_voc_detection_train"
    PASCAL_VOC_DETECTION_VAL = "pascal_voc_detection_val"
    ROBOFLOW_TRAIN_BASE = "roboflow_train_yolox"
    ROBOFLOW_VAL_BASE = "roboflow_val_yolox"


class Datasets:
    CIFAR_10 = "Cifar10"
    CIFAR_100 = "Cifar100"
    IMAGENET_DATASET = "ImageNetDataset"
    COCO_DETECTION_DATASET = "COCODetectionDataset"
    DETECTION_DATASET = "DetectionDataset"
    PASCAL_VOC_DETECTION_DATASET = "PascalVOCDetectionDataset"
    SEGMENTATION_DATASET = "SegmentationDataSet"
    COCO_SEGMENTATION_DATASET = "CoCoSegmentationDataSet"
    PASCAL_AUG_2012_SEGMENTATION_DATASET = "PascalAUG2012SegmentationDataSet"
    PASCAL_VOC_2012_SEGMENTATION_DATASET = "PascalVOC2012SegmentationDataSet"
    CITYSCAPES_DATASET = "CityscapesDataset"
    CITYSCAPES_CONCAT_DATASET = "CityscapesConcatDataset"
    MAPILLARY_DATASET = "MapillaryDataset"
    SUPERVISELY_PERSONS_DATASET = "SuperviselyPersonsDataset"
    PASCAL_VOC_AND_AUG_UNIFIED_DATASET = "PascalVOCAndAUGUnifiedDataset"
    COCO_KEY_POINTS_DATASET = "COCOKeypointsDataset"


class Processings:
    StandardizeImage = "StandardizeImage"
    DetectionCenterPadding = "DetectionCenterPadding"
    DetectionLongestMaxSizeRescale = "DetectionLongestMaxSizeRescale"
    DetectionBottomRightPadding = "DetectionBottomRightPadding"
    DetectionRescale = "DetectionRescale"
    KeypointsLongestMaxSizeRescale = "KeypointsLongestMaxSizeRescale"
    KeypointsBottomRightPadding = "KeypointsBottomRightPadding"
    ImagePermute = "ImagePermute"
    ReverseImageChannels = "ReverseImageChannels"
    NormalizeImage = "NormalizeImage"
    ComposeProcessing = "ComposeProcessing"
