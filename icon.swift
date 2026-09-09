import Foundation
import AppKit

func c(_ hex: UInt32) -> CGColor {
    CGColor(red: CGFloat((hex >> 16) & 0xFF)/255, green: CGFloat((hex >> 8) & 0xFF)/255,
            blue: CGFloat(hex & 0xFF)/255, alpha: 1)
}
let vert   = c(0x1E5B3D)
let creme  = c(0xFBFAF3)
let laiton = c(0xD2A748)

func draw(_ s: CGFloat, _ path: String) {
    let ctx = CGContext(data: nil, width: Int(s), height: Int(s), bitsPerComponent: 8,
                        bytesPerRow: 0, space: CGColorSpaceCreateDeviceRGB(),
                        bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
    ctx.setShouldAntialias(true)
    ctx.setFillColor(vert); ctx.fill(CGRect(x: 0, y: 0, width: s, height: s))

    // --- frettes : espacement décroissant vers le haut, c'est la signature d'un manche ---
    // y mesuré depuis le bas ; les cases se resserrent en montant
    let fretY: [CGFloat] = [0.045, 0.375, 0.655, 0.885].map { $0 * s }
    let fretH = s * 0.026

    // --- 6 cordes verticales, fines, de la plus grosse à la plus fine ---
    let inset = s * 0.175
    let gap   = (s - inset * 2) / 5
    let jauges: [CGFloat] = [0.0150, 0.0128, 0.0107, 0.0088, 0.0072, 0.0060]
    ctx.setFillColor(creme)
    for i in 0..<6 {
        let w = s * jauges[i]
        ctx.fill(CGRect(x: inset + gap * CGFloat(i) - w/2, y: 0, width: w, height: s))
    }
    for fy in fretY {
        ctx.fill(CGRect(x: 0, y: fy - fretH/2, width: s, height: fretH))
    }

    // --- repère de case, centré dans la case la plus large ---
    let cy = (fretY[1] + fretY[2]) / 2
    let r  = s * 0.088
    ctx.setFillColor(laiton)
    ctx.fillEllipse(in: CGRect(x: s/2 - r, y: cy - r, width: r*2, height: r*2))

    let rep = NSBitmapImageRep(cgImage: ctx.makeImage()!)
    try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: path))
}

for (size, name) in [(1024,"icon-1024"),(512,"icon-512"),(192,"icon-192"),
                     (180,"apple-touch-icon"),(32,"favicon-32")] {
    draw(CGFloat(size), "site/icons/\(name).png")
}

// planche de contrôle : l'icône à sa taille réelle sur l'écran d'accueil (60 pt), sur fond neutre
let W = 420.0, H = 150.0
let p = CGContext(data: nil, width: Int(W), height: Int(H), bitsPerComponent: 8, bytesPerRow: 0,
                  space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
p.setFillColor(c(0xE6E6E6)); p.fill(CGRect(x:0,y:0,width:W,height:H))
let src = NSImage(contentsOfFile: "site/icons/icon-512.png")!
var pr = CGRect(x:0,y:0,width:512,height:512)
let cg = src.cgImage(forProposedRect: &pr, context: nil, hints: nil)!
for (x, side) in [(20.0, 120.0), (170.0, 60.0), (260.0, 40.0), (330.0, 29.0)] {
    p.draw(cg, in: CGRect(x: x, y: (H - side)/2, width: side, height: side))
}
let rep2 = NSBitmapImageRep(cgImage: p.makeImage()!)
try! rep2.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "planche.png"))
print("ok")
