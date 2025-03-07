# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/models.ipynb.

# %% auto 0
__all__ = ['AutoRNN', 'AutoLSTM', 'AutoGRU', 'AutoTCN', 'AutoDilatedRNN', 'AutoMLP', 'AutoNBEATS', 'AutoNBEATSx', 'AutoNHITS',
           'AutoTFT', 'AutoVanillaTransformer', 'AutoInformer', 'AutoAutoformer', 'AutoFEDformer', 'AutoPatchTST',
           'AutoStemGNN', 'AutoHINT']

# %% ../nbs/models.ipynb 2
from os import cpu_count
import torch

from ray import tune
from ray.tune.search.basic_variant import BasicVariantGenerator

from .common._base_auto import BaseAuto

from .models.rnn import RNN
from .models.gru import GRU
from .models.tcn import TCN
from .models.lstm import LSTM
from .models.dilated_rnn import DilatedRNN

from .models.mlp import MLP
from .models.nbeats import NBEATS
from .models.nbeatsx import NBEATSx
from .models.nhits import NHITS

from .models.tft import TFT
from .models.vanillatransformer import VanillaTransformer
from .models.informer import Informer
from .models.autoformer import Autoformer
from .models.fedformer import FEDformer
from .models.patchtst import PatchTST

from .models.stemgnn import StemGNN
from .models.hint import HINT

from .losses.pytorch import MAE

# %% ../nbs/models.ipynb 8
class AutoRNN(BaseAuto):
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "inference_input_size_multiplier": [-1],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
    ):
        """Auto RNN

        **Parameters:**<br>

        """
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )
            config["inference_input_size"] = tune.choice(
                [h * x for x in self.default_config["inference_input_size_multiplier"]]
            )
            del (
                config["input_size_multiplier"],
                config["inference_input_size_multiplier"],
            )

        super(AutoRNN, self).__init__(
            cls_model=RNN,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
        )

# %% ../nbs/models.ipynb 12
class AutoLSTM(BaseAuto):
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "inference_input_size_multiplier": [-1],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )
            config["inference_input_size"] = tune.choice(
                [h * x for x in self.default_config["inference_input_size_multiplier"]]
            )
            del (
                config["input_size_multiplier"],
                config["inference_input_size_multiplier"],
            )

        super(AutoLSTM, self).__init__(
            cls_model=LSTM,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
        )

# %% ../nbs/models.ipynb 16
class AutoGRU(BaseAuto):
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "inference_input_size_multiplier": [-1],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )
            config["inference_input_size"] = tune.choice(
                [h * x for x in self.default_config["inference_input_size_multiplier"]]
            )
            del (
                config["input_size_multiplier"],
                config["inference_input_size_multiplier"],
            )

        super(AutoGRU, self).__init__(
            cls_model=GRU,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 19
class AutoTCN(BaseAuto):
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "inference_input_size_multiplier": [-1],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )
            config["inference_input_size"] = tune.choice(
                [h * x for x in self.default_config["inference_input_size_multiplier"]]
            )
            del (
                config["input_size_multiplier"],
                config["inference_input_size_multiplier"],
            )

        super(AutoTCN, self).__init__(
            cls_model=TCN,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 22
class AutoDilatedRNN(BaseAuto):
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "inference_input_size_multiplier": [-1],
        "h": None,
        "cell_type": tune.choice(["LSTM", "GRU"]),
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "dilations": tune.choice([[[1, 2], [4, 8]], [[1, 2, 4, 8]]]),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )
            config["inference_input_size"] = tune.choice(
                [h * x for x in self.default_config["inference_input_size_multiplier"]]
            )
            del (
                config["input_size_multiplier"],
                config["inference_input_size_multiplier"],
            )

        super(AutoDilatedRNN, self).__init__(
            cls_model=DilatedRNN,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 26
class AutoMLP(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([256, 512, 1024]),
        "num_layers": tune.randint(2, 6),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoMLP, self).__init__(
            cls_model=MLP,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 29
class AutoNBEATS(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoNBEATS, self).__init__(
            cls_model=NBEATS,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 32
class AutoNBEATSx(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoNBEATSx, self).__init__(
            cls_model=NBEATSx,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 35
class AutoNHITS(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "n_pool_kernel_size": tune.choice(
            [[2, 2, 1], 3 * [1], 3 * [2], 3 * [4], [8, 4, 1], [16, 8, 1]]
        ),
        "n_freq_downsample": tune.choice(
            [
                [168, 24, 1],
                [24, 12, 1],
                [180, 60, 1],
                [60, 8, 1],
                [40, 20, 1],
                [1, 1, 1],
            ]
        ),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.quniform(lower=500, upper=1500, q=100),
        "batch_size": tune.qloguniform(
            lower=5, upper=9, base=2, q=1
        ),  # [32, 64, 128, 256]
        "windows_batch_size": tune.qloguniform(
            lower=7, upper=10, base=2, q=1
        ),  # [128, 256, 512, 1024]
        "loss": None,
        "random_seed": tune.randint(lower=1, upper=20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoNHITS, self).__init__(
            cls_model=NHITS,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 39
class AutoTFT(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([64, 128, 256]),
        "n_head": tune.choice([4, 8]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoTFT, self).__init__(
            cls_model=TFT,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 42
class AutoVanillaTransformer(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([64, 128, 256]),
        "n_head": tune.choice([4, 8]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoVanillaTransformer, self).__init__(
            cls_model=VanillaTransformer,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 45
class AutoInformer(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([64, 128, 256]),
        "n_head": tune.choice([4, 8]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoInformer, self).__init__(
            cls_model=Informer,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 48
class AutoAutoformer(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([64, 128, 256]),
        "n_head": tune.choice([4, 8]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoAutoformer, self).__init__(
            cls_model=Autoformer,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 51
class AutoFEDformer(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice([64, 128, 256]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoFEDformer, self).__init__(
            cls_model=FEDformer,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 54
class AutoPatchTST(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3],
        "h": None,
        "hidden_size": tune.choice([16, 128, 256]),
        "n_head": tune.choice([4, 16]),
        "patch_len": tune.choice([16, 24]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "revin": tune.choice([False, True]),
        "max_steps": tune.choice([500, 1000, 5000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoPatchTST, self).__init__(
            cls_model=PatchTST,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 59
class AutoStemGNN(BaseAuto):
    default_config = {
        "input_size_multiplier": [1, 2, 3, 4],
        "h": None,
        "n_series": None,
        "n_stacks": tune.choice([2, 3]),
        "multi_layer": tune.choice([3, 5, 7]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "scaler_type": tune.choice([None, "robust", "standard"]),
        "max_steps": tune.choice([500, 1000, 2000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "loss": None,
        "random_seed": tune.randint(1, 20),
    }

    def __init__(
        self,
        h,
        n_series,
        loss=MAE(),
        valid_loss=None,
        config=None,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        refit_with_val=False,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        verbose=False,
        alias=None,
    ):
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()
            config["input_size"] = tune.choice(
                [h * x for x in self.default_config["input_size_multiplier"]]
            )

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config["step_size"] = tune.choice([1, h])
            del config["input_size_multiplier"]

        # Always use n_series from parameters
        config["n_series"] = n_series

        super(AutoStemGNN, self).__init__(
            cls_model=StemGNN,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )

# %% ../nbs/models.ipynb 63
class AutoHINT(BaseAuto):
    def __init__(
        self,
        cls_model,
        h,
        loss,
        valid_loss,
        S,
        config,
        search_alg=BasicVariantGenerator(random_state=1),
        num_samples=10,
        cpus=cpu_count(),
        gpus=torch.cuda.device_count(),
        refit_with_val=False,
        verbose=False,
        alias=None,
    ):
        super(AutoHINT, self).__init__(
            cls_model=cls_model,
            h=h,
            loss=loss,
            valid_loss=valid_loss,
            config=config,
            search_alg=search_alg,
            num_samples=num_samples,
            refit_with_val=refit_with_val,
            cpus=cpus,
            gpus=gpus,
            verbose=verbose,
            alias=alias,
        )
        # Validate presence of reconciliation strategy
        # parameter in configuration space
        if not ("reconciliation" in config.keys()):
            raise Exception(
                "config needs reconciliation, \
                            try tune.choice(['BottomUp', 'MinTraceOLS', 'MinTraceWLS'])"
            )
        self.S = S

    def _fit_model(self, cls_model, config, dataset, val_size, test_size):
        # Overwrite _fit_model for HINT two-stage instantiation
        reconciliation = config.pop("reconciliation")
        base_model = cls_model(**config)
        model = HINT(
            h=base_model.h, model=base_model, S=self.S, reconciliation=reconciliation
        )
        model.test_size = test_size
        model.fit(dataset, val_size=val_size, test_size=test_size)
        return model
