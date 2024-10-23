import argparse


def parameter_parser():
    # Experiment parameters
    parser = argparse.ArgumentParser(description='Smart Contracts Vulnerability Detection')

    parser.add_argument('-D', '--dataset', type=str, default='', choices=[])
    parser.add_argument('-M', '--model', type=str, default='EncoderWeight',
                        choices=['EncoderWeight', 'EncoderAttention', 'FNNModel'])#specifies model type
    parser.add_argument('--lr', type=float, default=0.001)#learning rate
    parser.add_argument('-d', '--dropout', type=float, default=0.2)#specifies dropout rate
    parser.add_argument('--epochs', type=int, default=5)#no.of times it is running
    parser.add_argument('-b', '--batch_size', type=int, default=32, help='batch size')

    return parser.parse_args()
