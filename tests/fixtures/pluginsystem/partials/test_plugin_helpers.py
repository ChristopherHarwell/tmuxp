import typing as t
from typing import Iterable, Mapping, Union

from tmuxp.plugin import TmuxpPlugin


class Config(t.TypedDict):
    tmux_version: t.Optional[str]
    tmuxp_version: t.Optional[str]
    libtmux_version: t.Optional[str]


class MyTestTmuxpPlugin(TmuxpPlugin):
    def __init__(self, config: Config) -> None:
        assert isinstance(config, dict)
        tmux_version = config.pop("tmux_version", None)
        libtmux_version = config.pop("libtmux_version", None)
        tmuxp_version = config.pop("tmuxp_version", None)

        TmuxpPlugin.__init__(self, **config)

        # WARNING! This should not be done in anything but a test
        if tmux_version:
            self.version_constraints["tmux"]["version"] = tmux_version
        if libtmux_version:
            self.version_constraints["libtmux"]["version"] = libtmux_version
        if tmuxp_version:
            self.version_constraints["tmuxp"]["version"] = tmuxp_version

        self._version_check()
