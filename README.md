The repository gives the trained models MoreMNAS A,B,C and D.

## How to reproduce & calculate metrics
```shell
$ python calculate.py --pb_path ./pretrained_model/MoreMNAS-A.pb
                      --save_path ./result/
```

## Comparison of some state-of-the-art SR Models

| Method | MulAdds| Params |Set5 | Set14 | BSD100 | Urban100 | 
| ------------- | ------------- |------------- |------------- |------------- |-------------|------------- |
| SRCNN  | 52.7G | 57K | 36.66/0.9542 | 32.42/0.9063 | 31.36/0.8879 | 29.50/0.8946 |
| FSRCNN | 6.0G | 12K | 37.00/0.9558 | 32.63/0.9088 | 31.53/0.8920 | 29.88/0.9020 |
| VDSR  | 612.6G | 665K | 37.53/0.9587 | 33.03/0.9124 | 31.90/0.8960 | 30.76/0.9140 |
| DRRN  | 6,796.9G | 297K | 37.74/0.9591 | 33.23/0.9136 | 32.05/0.8973 | 31.23/0.9188 |
| MoreMNAS-A (ours) | 238.6G | 1039K | 37.63/0.9584 | 33.23/0.9138 | 31.95/0.8961 | 31.24/0.9187|
| MoreMNAS-B (ours) | 256.9G | 1118K | 37.58/0.9584 | 33.22/0.9135 | 31.91/0.8959| 31.14/0.9175|
| MoreMNAS-C (ours) | 5.5G | 25K | 37.06/0.9561 | 32.75/0.9094| 31.50/0.8904 | 29.92/0.9023|
| MoreMNAS-D (ours) | 152.4G | 664K | 37.57/0.9584 | 33.25/0.9142 | 31.94/0.8966 | 31.25/0.9191|

## Qualitative results

Here are some results of MoreMNAS-A on Set 14. The complete result can be generated from the above mentions command.

![MoreMNAS-A set14 1](images/MoreMNAS-A/Set14/img_001_SRF_2_SR.png "MoreMNAS-A set14 001")

![MoreMNAS-A set14 2](images/MoreMNAS-A/Set14/img_005_SRF_2_SR.png "MoreMNAS-A set14 002")
