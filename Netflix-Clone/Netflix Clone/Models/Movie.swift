//
//  Movie.swift
//  Netflix Clone
//
//  Created by Little Asian Dude on 12/19/22.
//

import Foundation

struct TrendingTVResponse: Codable{
    let results: [Title]
}

struct TrendingMoviesResponse: Codable{
    let results: [Title]
}

struct UpcomingMoviesResponse: Codable{
    let results: [Title]
}

struct PopularMoviesResponse: Codable{
    let results: [Title]
}

struct TopRatedResponse: Codable{
    let results: [Title]
}

struct Title: Codable {
    let id: Int
    let media_type: String?
    let original_name: String?
    let original_title: String?
    let poster_path: String?
    let overview: String?
    let vote_count: Int
    let release_date: String?
    let vote_average: Double
}
