// @ts-ignore
import { CrumSort as _CrumSort } from "./crum-sort/crum-sort";

/**
 * Options used when initializing the bindings.
 */
export type LoadOptions = {
    /** Additional imports to be provided to the WebAssembly module */
    imports: WebAssembly.Imports,
    /**
     * A user-specified WebAssembly module to use instead of the one bundled
     * with this package.
     */
    module: WebAssembly.Module,
};

export default class Bindings {
    crum_sort(options?: Partial<LoadOptions>): Promise<_CrumSort>;
}