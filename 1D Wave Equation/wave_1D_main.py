import numpy as np
from sympy import Symbol, sin

import modulus.sym

from modulus.sym.hydra import instantiate_arch, ModulusConfig
from modulus.sym.solver import Solver
from modulus.sym.domain import Domain
from modulus.sym.geometry.primitives_1d import Line1D
from modulus.sym.domain.constraint import PointwiseBoundaryConstraint, PointwiseInteriorConstraint

from modulus.sym.domain.validator import PointwiseValidator
from modulus.sym.key import Key
from modulus.sym.node import Node
from wave_eq_main import WaveEquation1D