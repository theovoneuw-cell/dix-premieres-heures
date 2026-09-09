// Génère les icônes du site : un médiator blanc sur fond vert émeraude.
// Formes pleines et arrondies, pour coller à l'identité du site.
//   swift icon.swift
import Foundation
import AppKit

func c(_ hex: UInt32) -> CGColor {
    CGColor(red: CGFloat((hex >> 16) & 0xFF)/255,
            green: CGFloat((hex >> 8) & 0xFF)/255,
            blue: CGFloat(hex & 0xFF)/255, alpha: 1)
}
let fond   = c(0x0E9E68)   // émeraude — couleur du volet débutant
let mediat = c(0xFFFFFF)

func draw(_ s: CGFloat, _ chemin: String) {
    let x = CGContext(data: nil, width: Int(s), height: Int(s), bitsPerComponent: 8,
                      bytesPerRow: 0, space: CGColorSpaceCreateDeviceRGB(),
                      bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
    x.setShouldAntialias(true)
    x.setFillColor(fond)
    x.fill(CGRect(x: 0, y: 0, width: s, height: s))

    // Triangle isocèle : deux épaules très arrondies en haut, une pointe
    // resserrée en bas. C'est ce rapport de rayons qui fait le médiator —
    // des rayons égaux donnent une goutte, et un sommet trop rond une ampoule.
    let w = s * 0.62, h = s * 0.60
    let cx = s / 2, haut = s * 0.76, pointe = haut - h
    let gauche = CGPoint(x: cx - w/2, y: haut)
    let droite = CGPoint(x: cx + w/2, y: haut)
    let bas    = CGPoint(x: cx,       y: pointe)

    let p = CGMutablePath()
    p.move(to: CGPoint(x: cx, y: haut))
    p.addArc(tangent1End: droite, tangent2End: bas,    radius: s * 0.115)
    p.addArc(tangent1End: bas,    tangent2End: gauche, radius: s * 0.055)
    p.addArc(tangent1End: gauche, tangent2End: droite, radius: s * 0.115)
    p.closeSubpath()

    x.setFillColor(mediat)
    x.addPath(p)
    x.fillPath()

    let rep = NSBitmapImageRep(cgImage: x.makeImage()!)
    try! rep.representation(using: .png, properties: [:])!
        .write(to: URL(fileURLWithPath: chemin))
}

for (taille, nom) in [(1024, "icon-1024"), (512, "icon-512"), (192, "icon-192"),
                      (180, "apple-touch-icon"), (32, "favicon-32")] {
    draw(CGFloat(taille), "icons/\(nom).png")
}
print("icônes écrites dans icons/")
