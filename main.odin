package main

import "core:fmt"
import "core:os"
import "compiler"

main :: proc() {
    args := os.args
    if len(args) == 2{
        filename := args[1]
        if len(filename) < 3 || filename[len(filename)-2:] != ".a" {
            fmt.println("Error: File must be a-lang source file with .a extension")
            os.exit(1)
        }
        
        compiler.compile(filename)
    }

}