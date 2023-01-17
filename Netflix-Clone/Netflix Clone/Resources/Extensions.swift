//
//  Extensions.swift
//  Netflix Clone
//
//  Created by Little Asian Dude on 12/19/22.
//

import Foundation


extension String {
    func capitalizeFirstLetter() -> String{
        return self.prefix(1).uppercased() + self.lowercased().dropFirst()
    }
}
