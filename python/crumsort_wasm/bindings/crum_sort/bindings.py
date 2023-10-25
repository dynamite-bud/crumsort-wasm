from abc import abstractmethod
import ctypes
from typing import Any, Callable, List, Tuple, cast
import wasmer # type: ignore

try:
    from typing import Protocol
except ImportError:
    class Protocol: # type: ignore
        pass


def _load(make_view: Callable[[], Any], mem: wasmer.Memory, base: int, offset: int) -> Any:
    ptr = (base & 0xffffffff) + offset
    view = make_view()
    if ptr + view.bytes_per_element > mem.data_size:
        raise IndexError('out-of-bounds load')
    view_ptr = ptr // view.bytes_per_element
    return view[view_ptr]

def _list_canon_lift(ptr: int, len: int, size: int, make_view: Callable[[], Any], mem: wasmer.Memory) -> Any:
    ptr = ptr & 0xffffffff
    len = len & 0xffffffff
    if ptr + len * size > mem.data_size:
        raise IndexError('list out of bounds')
    view = make_view()
    assert(size == view.bytes_per_element)
    view_ptr = ptr // view.bytes_per_element
    if isinstance(view, wasmer.Uint8Array):
        return bytearray(view[view_ptr:view_ptr+len])
    return view[view_ptr:view_ptr + len]

def _list_canon_lower(list: Any, make_view: Callable[[], Any], size: int, align: int, realloc: wasmer.Function, mem: wasmer.Memory) -> Tuple[int, int]:
    total_size = size * len(list)
    ptr = realloc(0, 0, align, total_size)
    assert(isinstance(ptr, int))
    ptr = ptr & 0xffffffff
    if ptr + total_size > mem.data_size:
        raise IndexError('list realloc return of bounds')
    view = make_view()
    assert(size == view.bytes_per_element)
    view_ptr = ptr // view.bytes_per_element
    view[view_ptr:view_ptr + len(list)] = list
    return (ptr, len(list))
class CrumSort:
    instance: wasmer.Instance
    _canonical_abi_free: wasmer.Function
    _canonical_abi_realloc: wasmer.Function
    _memory: wasmer.Memory
    _par_crumsort_i16: wasmer.Function
    _par_crumsort_i32: wasmer.Function
    _par_crumsort_i64: wasmer.Function
    _par_crumsort_i8: wasmer.Function
    _par_crumsort_u16: wasmer.Function
    _par_crumsort_u32: wasmer.Function
    _par_crumsort_u64: wasmer.Function
    _par_crumsort_u8: wasmer.Function
    def __init__(self, store: wasmer.Store, imports: dict[str, dict[str, Any]], module: wasmer.Module):
        self.instance = wasmer.Instance(module, imports)
        
        canonical_abi_free = self.instance.exports.__getattribute__('canonical_abi_free')
        assert(isinstance(canonical_abi_free, wasmer.Function))
        self._canonical_abi_free = canonical_abi_free
        
        canonical_abi_realloc = self.instance.exports.__getattribute__('canonical_abi_realloc')
        assert(isinstance(canonical_abi_realloc, wasmer.Function))
        self._canonical_abi_realloc = canonical_abi_realloc
        
        memory = self.instance.exports.__getattribute__('memory')
        assert(isinstance(memory, wasmer.Memory))
        self._memory = memory
        
        par_crumsort_i16 = self.instance.exports.__getattribute__('par-crumsort-i16')
        assert(isinstance(par_crumsort_i16, wasmer.Function))
        self._par_crumsort_i16 = par_crumsort_i16
        
        par_crumsort_i32 = self.instance.exports.__getattribute__('par-crumsort-i32')
        assert(isinstance(par_crumsort_i32, wasmer.Function))
        self._par_crumsort_i32 = par_crumsort_i32
        
        par_crumsort_i64 = self.instance.exports.__getattribute__('par-crumsort-i64')
        assert(isinstance(par_crumsort_i64, wasmer.Function))
        self._par_crumsort_i64 = par_crumsort_i64
        
        par_crumsort_i8 = self.instance.exports.__getattribute__('par-crumsort-i8')
        assert(isinstance(par_crumsort_i8, wasmer.Function))
        self._par_crumsort_i8 = par_crumsort_i8
        
        par_crumsort_u16 = self.instance.exports.__getattribute__('par-crumsort-u16')
        assert(isinstance(par_crumsort_u16, wasmer.Function))
        self._par_crumsort_u16 = par_crumsort_u16
        
        par_crumsort_u32 = self.instance.exports.__getattribute__('par-crumsort-u32')
        assert(isinstance(par_crumsort_u32, wasmer.Function))
        self._par_crumsort_u32 = par_crumsort_u32
        
        par_crumsort_u64 = self.instance.exports.__getattribute__('par-crumsort-u64')
        assert(isinstance(par_crumsort_u64, wasmer.Function))
        self._par_crumsort_u64 = par_crumsort_u64
        
        par_crumsort_u8 = self.instance.exports.__getattribute__('par-crumsort-u8')
        assert(isinstance(par_crumsort_u8, wasmer.Function))
        self._par_crumsort_u8 = par_crumsort_u8
    def par_crumsort_u8(self, arr: bytes) -> bytes:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.uint8_view, 1, 1, realloc, memory)
        ret = self._par_crumsort_u8(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(bytes, _list_canon_lift(ptr2, len3, 1, memory.uint8_view, memory))
        free(ptr2, len3, 1)
        return list
    def par_crumsort_u16(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.uint16_view, 2, 2, realloc, memory)
        ret = self._par_crumsort_u16(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 2, memory.uint16_view, memory))
        free(ptr2, len3, 2)
        return list
    def par_crumsort_u32(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.uint32_view, 4, 4, realloc, memory)
        ret = self._par_crumsort_u32(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 4, memory.uint32_view, memory))
        free(ptr2, len3, 4)
        return list
    def par_crumsort_u64(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.uint64_view, 8, 8, realloc, memory)
        ret = self._par_crumsort_u64(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 8, memory.uint64_view, memory))
        free(ptr2, len3, 8)
        return list
    def par_crumsort_i8(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.int8_view, 1, 1, realloc, memory)
        ret = self._par_crumsort_i8(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 1, memory.int8_view, memory))
        free(ptr2, len3, 1)
        return list
    def par_crumsort_i16(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.int16_view, 2, 2, realloc, memory)
        ret = self._par_crumsort_i16(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 2, memory.int16_view, memory))
        free(ptr2, len3, 2)
        return list
    def par_crumsort_i32(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.int32_view, 4, 4, realloc, memory)
        ret = self._par_crumsort_i32(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 4, memory.int32_view, memory))
        free(ptr2, len3, 4)
        return list
    def par_crumsort_i64(self, arr: List[int]) -> List[int]:
        memory = self._memory;
        realloc = self._canonical_abi_realloc
        free = self._canonical_abi_free
        ptr, len0 = _list_canon_lower(arr, memory.int64_view, 8, 8, realloc, memory)
        ret = self._par_crumsort_i64(ptr, len0)
        assert(isinstance(ret, int))
        load = _load(memory.int32_view, memory, ret, 0)
        load1 = _load(memory.int32_view, memory, ret, 4)
        ptr2 = load
        len3 = load1
        list = cast(List[int], _list_canon_lift(ptr2, len3, 8, memory.int64_view, memory))
        free(ptr2, len3, 8)
        return list
