---
title: "If You are not Satisfied You Could Further Reduce Tauri Executable Size"
date: 2025-12-24 
categories: [Tutorial, Desktop App Framework]
tags: [tauri, electron, rust, javascript, nodejs, pyhon]
image: /assets/img/2025-12-24/Tauri-default-screen.png
---

In the past we saw that a vanilla Tauri executable is just 18 mb and installer size is 6 mb. This is far far smaller than electron which is typically over 100 mb. However if you want you could even further reduce it to the insane level.
Here are the ways:

## Optimize Rust Build Settings

In your src-tauri/Cargo.toml, add or update the [profile.release] section. These settings instruct the compiler to prioritize binary size over compilation speed.

```rust
[profile.release]
panic = "abort"      # Disables stack unwinding; saves space
codegen-units = 1    # Allows better optimization by compiling as one unit
lto = true           # Enables Link-Time Optimization for cross-crate optimization
opt-level = "z"      # "s" (size) or "z" (even smaller)
strip = true         # Automatically removes debug symbols from the binary
```

Now run again

```batch
 npm run tauri build
 ```

Now installer will be **1.83 mb** and executable will be **3 mb**. Impressive, hah!

## Configure Tauri Features

In tauri.conf.json, only enable the API features you actually use. Disabling unused modules prevents them from being compiled into your final app

## Frontend Asset Optimization

The frontend bundle is often a major contributor to file size.

### Minify Code

Ensure your bundler (Vite, Webpack, etc.) is configured for production minification and tree-shaking

### Disable Source Maps

Source maps are for debugging and are unnecessary "dead weight" in production.

### Optimize Media

Use modern formats like .webp or .avif for images and remove metadata from camera files

### Use System Fonts

Instead of bundling large custom fonts, use system font stacks

## Post-Build Compression (UPX)

## UPX

For the smallest possible file, use UPX (Ultimate Packer for eXecutables) to compress the final .exe. UPX is designed specifically for executables and shared libraries, not for installers. 
Command: 

```batch
upx --ultra-brute src-tauri/target/release/your_app.exe
```

or unzip upx add to PATH its binary. then 


## cargo-bloat

It is a Rust utility used to analyze and reduce the size of your application's binary, and it works with Tauri projects just like any other Rust application. It helps identify which crates or functions are taking up the most space, a key step in keeping Tauri apps lightweight.
To use cargo-bloat, you must first install it globally using Cargo:

```batch
cargo install cargo-bloat
```

Navigate to the `src-tauri` directory of your Tauri project, which contains the Cargo.toml file, and run the command. The most common use case is analyzing the release build

```batch
cargo bloat --release
```

Common flags:
--release: Analyzes the optimized release build, which is what end-users receive.
--crates: Shows the size breakdown per crate/dependency.
-n <NUM>: Limits the output to a specified number of lines (e.g., -n 20). 

## Stripping

Use strip utilities to remove debug symbols from your compiled app.
Your compiled app includes so-called "Debug Symbols" that include function and variable names. Your end-users will probably not care about Debug Symbols, so this is a pretty surefire way to save some bytes!

cargo.Toml

[profile.release]
strip = true  # Automatically strip symbols from the binary.