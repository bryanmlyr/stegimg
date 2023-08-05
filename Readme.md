# Stegimg
## Description
The goal of this small project is to encode/decode ascii characters with colors' bytes.

### How does it work?
Example for: "Hello, world"

```
R: H -> 72
G: e -> 101
B: l -> 108

R: l -> 108
G: o -> 111
B: , -> 44

R:   -> 32
G: w -> 119
B: o -> 111

R: r -> 114
G: l -> 108
B: d -> 100
```

The result should be (zoom it):

![Hello world result](./example/hw.png)
