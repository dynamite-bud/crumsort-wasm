'''
Bindings to the  library.
'''

from pathlib import Path
from typing import Optional, Any

from wasmer import Store, Module, wasi # type: ignore
from .crum_sort.bindings import (
    CrumSort as _CrumSort,
)

class Bindings:
    """
    Instantiate bindings to the various libraries in this package.
    """

    def __init__(self, store: Store):
        self._store = store
        self._cache: dict[str, Module] = {}

    def _get_module(self, filename: str) -> Module:
        if filename in self._cache:
            return self._cache[filename]

        wasm = Path(__file__).parent.joinpath(filename).read_bytes()
        module = Module(self._store, wasm)
        self._cache[filename] = module
        return module

    def crum_sort(
        self,
        module: Optional[Module] = None,
    ) -> _CrumSort:
        """
        Instantiate the "crum_sort" library.
        :param module: A user-specified WebAssembly module to use instead of the
                       one bundled with this package.
        """

        filename = "crum_sort/crumsort-wasm.wasm"
        if not module:
            module = self._get_module(filename)

        imports: dict[str, Any] = {}

        wrapper = None

        def get_export(item_name: str):
            assert wrapper is not None
            return getattr(wrapper.instance.exports, item_name)

        wrapper = _CrumSort(self._store, imports, module)
        return wrapper
    