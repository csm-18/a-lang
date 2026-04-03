package compiler

import "core:fmt"
import "core:os"

compile :: proc(filename: string) {
    sourceCode := readSourceFile(filename)
    fmt.println(sourceCode)
}

readSourceFile :: proc(filename: string) -> string {
    allocator := context.allocator

    data, ok := os.read_entire_file(filename, allocator)
    if ok != nil {
        fmt.println("Error: Could not read file: ", filename)
        os.exit(1)
    }
    // free happens automatically if allocator is temp
    
    return string(data)
}