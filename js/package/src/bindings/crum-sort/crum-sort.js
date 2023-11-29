const { data_view } = require('./intrinsics.js');
class CrumSort {
  addToImports(imports) {
  }
  
  async instantiate(module, imports) {
    imports = imports || {};
    this.addToImports(imports);
    
    if (module instanceof WebAssembly.Instance) {
      this.instance = module;
    } else if (module instanceof WebAssembly.Module) {
      this.instance = await WebAssembly.instantiate(module, imports);
    } else if (module instanceof ArrayBuffer || module instanceof Uint8Array) {
      const { instance } = await WebAssembly.instantiate(module, imports);
      this.instance = instance;
    } else {
      const { instance } = await WebAssembly.instantiateStreaming(module, imports);
      this.instance = instance;
    }
    this._exports = this.instance.exports;
  }
  parCrumsortU8(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 1, len0 * 1);
    (new Uint8Array(memory.buffer, ptr0, len0 * 1)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 1));
    const ret = this._exports['par-crumsort-u8'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Uint8Array(memory.buffer.slice(ptr1, ptr1 + len1 * 1));
    free(ptr1, len1, 1);
    return list1;
  }
  parCrumsortU16(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 2, len0 * 2);
    (new Uint8Array(memory.buffer, ptr0, len0 * 2)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 2));
    const ret = this._exports['par-crumsort-u16'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Uint16Array(memory.buffer.slice(ptr1, ptr1 + len1 * 2));
    free(ptr1, len1, 2);
    return list1;
  }
  parCrumsortU32(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 4, len0 * 4);
    (new Uint8Array(memory.buffer, ptr0, len0 * 4)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 4));
    const ret = this._exports['par-crumsort-u32'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Uint32Array(memory.buffer.slice(ptr1, ptr1 + len1 * 4));
    free(ptr1, len1, 4);
    return list1;
  }
  parCrumsortU64(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 8, len0 * 8);
    (new Uint8Array(memory.buffer, ptr0, len0 * 8)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 8));
    const ret = this._exports['par-crumsort-u64'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new BigUint64Array(memory.buffer.slice(ptr1, ptr1 + len1 * 8));
    free(ptr1, len1, 8);
    return list1;
  }
  parCrumsortI8(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 1, len0 * 1);
    (new Uint8Array(memory.buffer, ptr0, len0 * 1)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 1));
    const ret = this._exports['par-crumsort-i8'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Int8Array(memory.buffer.slice(ptr1, ptr1 + len1 * 1));
    free(ptr1, len1, 1);
    return list1;
  }
  parCrumsortI16(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 2, len0 * 2);
    (new Uint8Array(memory.buffer, ptr0, len0 * 2)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 2));
    const ret = this._exports['par-crumsort-i16'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Int16Array(memory.buffer.slice(ptr1, ptr1 + len1 * 2));
    free(ptr1, len1, 2);
    return list1;
  }
  parCrumsortI32(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 4, len0 * 4);
    (new Uint8Array(memory.buffer, ptr0, len0 * 4)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 4));
    const ret = this._exports['par-crumsort-i32'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new Int32Array(memory.buffer.slice(ptr1, ptr1 + len1 * 4));
    free(ptr1, len1, 4);
    return list1;
  }
  parCrumsortI64(arg0) {
    const memory = this._exports.memory;
    const realloc = this._exports["canonical_abi_realloc"];
    const free = this._exports["canonical_abi_free"];
    const val0 = arg0;
    const len0 = val0.length;
    const ptr0 = realloc(0, 0, 8, len0 * 8);
    (new Uint8Array(memory.buffer, ptr0, len0 * 8)).set(new Uint8Array(val0.buffer, val0.byteOffset, len0 * 8));
    const ret = this._exports['par-crumsort-i64'](ptr0, len0);
    const ptr1 = data_view(memory).getInt32(ret + 0, true);
    const len1 = data_view(memory).getInt32(ret + 4, true);
    const list1 = new BigInt64Array(memory.buffer.slice(ptr1, ptr1 + len1 * 8));
    free(ptr1, len1, 8);
    return list1;
  }
}

module.exports = { CrumSort };
