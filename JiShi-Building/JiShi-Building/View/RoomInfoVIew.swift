//
//  RoomInfoVIew.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI

struct RoomInfoVIew: View {
    
    @Environment(\.presentationMode) var presentationMode
    

    let roomNum: String
    
    let keyWord: [String]
    
    let description: String
    
    var body: some View {
        GeometryReader{proxy in
                    
            let width = proxy.size.width
            let height = proxy.size.height
            
            
                    
            VStack(alignment: .leading){
                Image(roomNum)
                    .resizable()
                    .frame(width: width, height: height/2, alignment: .center)
                    .foregroundColor(.green)
                    .onTapGesture(count: 1) {
                        self.presentationMode.wrappedValue.dismiss()
                    }
                        
                HStack{
                        
                    Text(roomNum)
                        .font(.system(.largeTitle, design: .rounded))
                        .fontWeight(.heavy)
                        .lineLimit(3)
                        .multilineTextAlignment(.leading)
                        .padding(10)
                        .minimumScaleFactor(0.5)
                        .lineLimit(1)
                    Spacer()
                            
                    ForEach(keyWord, id: \.self){ word in
                        Text(word)
                            .lineLimit(1)
                            .font(.headline)
                            .foregroundColor(.white)
                            .padding(4)
                            .background(.gray)
                            .cornerRadius(5)

                    }
                    .padding()
                }
                
                        
                Divider()
                
                Text(description)
                    .padding(.horizontal,10)
                    .font(.body)
                
                Spacer()
                
                Divider()
                
                Text("请点击图片退出")
                    .font(.footnote)
                    .foregroundColor(.gray)
                    .frame(width: width)
                
                        

                        
                        
            }
            .frame(width: width, height: height, alignment: .center)
        }
    }
}

struct RoomInfoVIew_Previews: PreviewProvider {
    
    
    static var previews: some View {
        RoomInfoVIew(roomNum: "407L", keyWord: ["实验室","张荣庆"], description: "kajsdhajkdhajkdhakjd")
    }
}
