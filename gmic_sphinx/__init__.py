__all__ = ["GmicPic", "setup"]

from .gmicpic import GmicPic


def setup(app):
    """Setup directive"""
    app.add_directive("gmicpic", GmicPic)

