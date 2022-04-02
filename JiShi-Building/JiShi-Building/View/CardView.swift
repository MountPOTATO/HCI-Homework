//
//  CardView.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI

struct CardView: View {
    
    let roomNum:String
    
    var body: some View {
        VStack(alignment:.leading, spacing: 10){
            Image(roomNum)
                .resizable()
            cardText.padding(.horizontal,5)
        }
        .clipShape(RoundedRectangle(cornerRadius: 5))
        .foregroundColor(.black)
        .overlay(
            RoundedRectangle(cornerRadius: 5)
            .stroke(Color.gray, lineWidth: 2)
        )
    }
    
    var cardText: some View{
        VStack(alignment:.leading){
            HStack{
                Image(systemName: "house")
                Text(roomNum)
                    .font(.footnote)
                    .lineLimit(1)
                    .minimumScaleFactor(0.1) //<--Here
                
            }
            .padding(.bottom,5)
            
        }
    }
}

struct CardView_Previews: PreviewProvider {
    static var previews: some View {
        CardView(roomNum: "407L")
    }
}

