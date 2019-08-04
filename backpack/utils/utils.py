"""Utility functions."""

import torch
import opt_einsum as oe

TORCH = "torch"
OPT_EINSUM = "opt_einsum"

BPEXTS_EINSUM = "torch"


def _oe_einsum(equation, *operands):
    # handle old interface, passing operands as one list
    # see https://pytorch.org/docs/stable/_modules/torch/functional.html#einsum
    if len(operands) == 1 and isinstance(operands[0], (list, tuple)):
        operands = operands[0]
    return oe.contract(equation, *operands, backend='torch')


EINSUMS = {
    TORCH: torch.einsum,
    OPT_EINSUM: _oe_einsum,
}


def einsum(equation, *operands):
    """`einsum` implementations used by `backpack`.

    Modify by setting `backpack.utils.utils.BPEXTS_EINSUM`.
    See `backpack.utils.utils.EINSUMS` for supported implementations.
    """
    return EINSUMS[BPEXTS_EINSUM](equation, *operands)