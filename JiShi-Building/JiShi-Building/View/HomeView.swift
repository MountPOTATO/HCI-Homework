//
//  HomeView.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI



struct HomeView: View {
    
    
    @State private var isPresented = false
    
    var body: some View {
        GeometryReader{ proxy in
            let width = proxy.size.width
            let height = proxy.size.width
            
            var currentChosed = ""
            
            Form{
                
                
                Section{
                    Text("Jishi Building Floor 4th")
                        .font(.headline)
                        .fontWeight(.heavy)
                        .minimumScaleFactor(0.5)
                        .lineLimit(1)

                    Text("Address: Shanghai, China, along road 4800, tongji university software institute")

                }
                
                                
                Section{
                    Text("West Corridor")
                        .font(.subheadline)
                        .fontWeight(.bold)
                        .minimumScaleFactor(0.5)
                        .lineLimit(1)
                    
                    ScrollView(.horizontal){
                        HStack{
                            ForEach(westCorridor, id:\.self){ roomID in
                                
                                Button(action: {
                                    self.isPresented = true
                                    currentChosed = roomID

                                }, label: {
                                    CardView(roomNum: roomID)
                                        .frame(width: width/3.5, height: height/4, alignment: .center)
                                }).sheet(isPresented: $isPresented, content: {
                                    RoomInfoVIew(roomNum: currentChosed, keyWord: keyDict[currentChosed]!, description: descriptionDict[currentChosed]!)
                                })
                                .padding(.leading,2)
                                .padding(.bottom,1)
          
                            }
                        }
                    }
                    .padding(.bottom,3)
               
                }
                
                Section{
                    Text("North Corridor")
                        .font(.subheadline)
                        .fontWeight(.bold)
                        .minimumScaleFactor(0.5)
                        .lineLimit(1)
                    
                    ScrollView(.horizontal){
                        HStack{
                            ForEach(northCorridor, id:\.self){ roomID in
                                
                                Button(action: {
                                    self.isPresented = true
                                    currentChosed = roomID

                                }, label: {
                                    CardView(roomNum: roomID)
                                        .frame(width: width/3.5, height: height/4, alignment: .center)
                                }).sheet(isPresented: $isPresented, content: {
                                    RoomInfoVIew(roomNum: currentChosed, keyWord: keyDict[currentChosed]!, description: descriptionDict[currentChosed]!)
                                })
                                .padding(.leading,2)
                                .padding(.bottom,1)
          
                            }
                        }
                    }
                    .padding(.bottom,3)
               
                }
                
                Section{
                    Text("East Corridor")
                        .font(.subheadline)
                        .fontWeight(.bold)
                        .minimumScaleFactor(0.5)
                        .lineLimit(1)
                    
                    ScrollView(.horizontal){
                        HStack{
                            ForEach(eastCorridor, id:\.self){ roomID in
                                
                                Button(action: {
                                    self.isPresented = true
                                    currentChosed = roomID

                                }, label: {
                                    CardView(roomNum: roomID)
                                        .frame(width: width/3.5, height: height/4, alignment: .center)
                                }).sheet(isPresented: $isPresented, content: {
                                    RoomInfoVIew(roomNum: currentChosed, keyWord: keyDict[currentChosed]!, description: descriptionDict[currentChosed]!)
                                })
                                .padding(.leading,2)
                                .padding(.bottom,1)
          
                            }
                        }
                    }
                    .padding(.bottom,3)
               
                }
                
                

            }
            .cornerRadius(5).clipped()


            
            

        }
    }
}

struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView()
    }
}
