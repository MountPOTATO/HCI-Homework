//
//  SearchView.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI

struct SearchBar: View{
    
    @Binding var text:String
    
    @State private var isEditing = false
    
    var body: some View{
        HStack{
            TextField("Search...",text: $text)
                .padding(7)
                .padding(.horizontal,25)
                .background(Color(.systemGray6))
                .cornerRadius(8)
                .overlay(
                    HStack {
                        Image(systemName: "magnifyingglass")
                            .foregroundColor(.gray)
                            .frame(minWidth: 0, maxWidth: .infinity, alignment: .leading)
                            .padding(.leading, 8)
                        if isEditing {
                            Button(action: {
                                self.text = ""
                            }) {
                                Image(systemName: "multiply.circle.fill")
                                    .foregroundColor(.gray)
                                    .padding(.trailing, 8)
                            }
                        }
                    }
                )
                .padding(.horizontal,10)
                .onTapGesture {
                    self.isEditing = true
                }
            
            if isEditing {
                Button {
                    self.isEditing = false
                    self.text = ""
                    
                    // 关闭键盘
                    UIApplication.shared.sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
                    
                } label: {
                    Text("Cancel")
                }
                .padding(.trailing,10)
                .transition(.move(edge: .trailing))

            }
            
        }
    }
    
}

struct SearchView: View {
    
    @State private var searchText = ""
    
    @State private var newViewPresented = false
    
    func foundKeyWord(_ keyWord:String)->Bool {
        for i in keyDict[keyWord]!{
            if i.contains(keyWord){
                return true
            }
        }
        return false
    }
    
    var body: some View {
        
//        var currentChosed: String = ""
        
        GeometryReader{proxy in
            let width = proxy.size.width
            let height = proxy.size.width
            
            
            VStack(alignment: .leading){
                Text("Search")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .foregroundColor(.blue)
                    .padding()
                


                SearchBar(text: $searchText)
                        .padding(.top,-10)
                
                List(totalRoom.filter({ searchText.isEmpty ? false : ($0.contains(searchText)||foundKeyWord($0)) }), id: \.self){  item in
                    
                    
                    Button {
                        self.newViewPresented = true
                    } label: {
                        HStack{
                            Image(item)
                                .resizable()
                                .frame(width: width/4, height: height/5, alignment: .center)
                            Spacer()
                            VStack(alignment: .trailing){
                                
                                HStack{
                                    Image(systemName: "house")
                                    Text(item)
                                        .minimumScaleFactor(0.1) //<--Here
                                        .lineLimit(1)
                                }
                                
                                HStack{
                                    ForEach(keyDict[item]!, id: \.self){ word in
                                        Text(word)
                                            .lineLimit(1)
                                            .font(.system(size:10))
                                            .foregroundColor(.white)
                                            .minimumScaleFactor(0.1) //<--Here
                                            .padding(4)
                                            .background(.gray)
                                            .cornerRadius(5)                                        

                                    }
                                }
                                
                                
                            }
                            .padding()
                        }
                        .clipShape(RoundedRectangle(cornerRadius: 5))
                        .foregroundColor(.black)
                        .overlay(
                            RoundedRectangle(cornerRadius: 5)
                            .stroke(Color.gray, lineWidth: 2)
                        )
                    }.sheet(isPresented: $newViewPresented) {
                        RoomInfoVIew(roomNum: item, keyWord: keyDict[item]!, description: descriptionDict[item]!)
                    }
                    .padding()

                    
                    
                    
                }
            }
            .padding()
    
            

                
                    
            
        }
        

    }
}

struct SearchView_Previews: PreviewProvider {
    static var previews: some View {
        SearchView()
    }
}
