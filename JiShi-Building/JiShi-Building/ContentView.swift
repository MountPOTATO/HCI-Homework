//
//  ContentView.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI

struct ContentView: View {
    
    var body: some View {
        TabView{
            HomeView()
                .tabItem {
                    Text("Home")
                    Image(systemName: "house.fill")
                }
            JiShiMapView()
                .tabItem {
                    Text("Map")
                    Image(systemName: "map.fill")
                }
            SearchView()
                .tabItem {
                    Text("Search")
                    Image(systemName: "magnifyingglass.circle.fill")
                }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
