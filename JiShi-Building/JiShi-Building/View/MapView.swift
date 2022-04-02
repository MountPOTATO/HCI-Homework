//
//  MapView.swift
//  JiShi-Building
//
//  Created by mount_potato on 2022/4/1.
//

import SwiftUI
import UIKit
import MapKit


struct Pin: Identifiable {
    let id = UUID()
    var name: String
}




struct UIViewMap: UIViewRepresentable {


    
    
    var didSelect: (MKPointAnnotation) -> ()



    func makeUIView(context: UIViewRepresentableContext<UIViewMap>) -> MKMapView {
        return MKMapView()
    }

    func updateUIView(_ uiView: MKMapView, context: UIViewRepresentableContext<UIViewMap>) {

        uiView.delegate = context.coordinator

        uiView.isZoomEnabled = false
        uiView.isScrollEnabled = false
        uiView.isRotateEnabled = false

        uiView.mapType = MKMapType.hybrid

        let coordinate2D = CLLocationCoordinate2D(latitude: 31.283770, longitude: 121.20980)

        let zoomLevel = 0.001

        let region = MKCoordinateRegion(center: coordinate2D, span: MKCoordinateSpan(latitudeDelta: zoomLevel, longitudeDelta: zoomLevel))


        uiView.setRegion(uiView.regionThatFits(region), animated: true)

        
        let coord_sz = CLLocationCoordinate2D(latitude: 31.28335, longitude: 121.20992)
        let annotation_sz = MKPointAnnotation()
        annotation_sz.coordinate = coord_sz
        annotation_sz.title = "Sports Zone"
        uiView.addAnnotation(annotation_sz)

        let coord_407 = CLLocationCoordinate2D(latitude: 31.28355, longitude: 121.20975)
        let annotation_407 = MKPointAnnotation()
        annotation_407.coordinate = coord_407
        annotation_407.title = "407"
        uiView.addAnnotation(annotation_407)
        
        
        let coord_408 = CLLocationCoordinate2D(latitude: 31.28346, longitude: 121.20966)
        let annotation_408 = MKPointAnnotation()
        annotation_408.coordinate = coord_408
        annotation_408.title = "408"
        uiView.addAnnotation(annotation_408)

        

        let coord_409 = CLLocationCoordinate2D(latitude: 31.28363, longitude: 121.20966)
        let annotation_409 = MKPointAnnotation()
        annotation_409.coordinate = coord_409
        annotation_409.title = "409"
        uiView.addAnnotation(annotation_409)
        
        let coord_414 = CLLocationCoordinate2D(latitude: 31.28378, longitude: 121.20939)
        let annotation_414 = MKPointAnnotation()
        annotation_414.coordinate = coord_414
        annotation_414.title = "414"
        uiView.addAnnotation(annotation_414)
        
        
        let coord_417 = CLLocationCoordinate2D(latitude: 31.28388, longitude: 121.20958)
        
        let annotation_417 = MKPointAnnotation()
        annotation_417.coordinate = coord_417
        annotation_417.title = "417"
        uiView.addAnnotation(annotation_417)

        
        let coord_426 = CLLocationCoordinate2D(latitude: 31.2842, longitude: 121.20954)
        let annotation_426 = MKPointAnnotation()
        annotation_426.coordinate = coord_426
        annotation_426.title = "426"
        uiView.addAnnotation(annotation_426)
        
        let coord_430 = CLLocationCoordinate2D(latitude: 31.2842, longitude: 121.20969)
        let annotation_430 = MKPointAnnotation()
        annotation_430.coordinate = coord_430
        annotation_430.title = "430"
        uiView.addAnnotation(annotation_430)
        
        let coord_chess = CLLocationCoordinate2D(latitude: 31.2841, longitude: 121.20975)
        let annotation_chess = MKPointAnnotation()
        annotation_chess.coordinate = coord_chess
        annotation_chess.title = "Chess Zone"
        uiView.addAnnotation(annotation_chess)
        
        
        let coord_434 = CLLocationCoordinate2D(latitude: 31.2842, longitude: 121.20987)
        let annotation_434 = MKPointAnnotation()
        annotation_434.coordinate = coord_434
        annotation_434.title = "434"
        uiView.addAnnotation(annotation_434)
        
        let coord_442 = CLLocationCoordinate2D(latitude: 31.2840, longitude: 121.20987)
        let annotation_442 = MKPointAnnotation()
        annotation_442.coordinate = coord_442
        annotation_442.title = "442"
        uiView.addAnnotation(annotation_442)
        
        let coord_446 = CLLocationCoordinate2D(latitude: 31.28383, longitude: 121.20989)
        let annotation_446 = MKPointAnnotation()
        annotation_446.coordinate = coord_446
        annotation_446.title = "448"
        uiView.addAnnotation(annotation_446)
        
        let coord_452 = CLLocationCoordinate2D(latitude: 31.28374, longitude: 121.20995)
        let annotation_452 = MKPointAnnotation()
        annotation_452.coordinate = coord_452
        annotation_452.title = "452"
        uiView.addAnnotation(annotation_452)
        
        let coord_of = CLLocationCoordinate2D(latitude: 31.28373, longitude: 121.2102)
        let annotation_of = MKPointAnnotation()
        annotation_of.coordinate = coord_of
        annotation_of.title = "Dean Room"
        uiView.addAnnotation(annotation_of)
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

}



class Coordinator: NSObject, MKMapViewDelegate {

    var parent: UIViewMap


    init(_ sFMapView: UIViewMap) {
        self.parent = sFMapView
        super.init()

    }

    /// This is where the delegate gets the object for the selected annotation
    func mapView(_ mapView: MKMapView, didSelect view: MKAnnotationView) {
        if let v = view.annotation  {
            print(v.coordinate)
            self.parent.didSelect(v as! MKPointAnnotation)
        }
    }


}


struct JiShiMapView: View{
    @State var selectItem: Pin?
    var body: some View{

        UIViewMap(){annotation in
            self.selectItem = Pin(name: annotation.title!)
        }
        .sheet(item: self.$selectItem){ item in
            RoomInfoVIew(roomNum: item.name, keyWord: keyDict[item.name]!, description: descriptionDict[item.name]!)
        }
    }
}



struct MapView_Previews: PreviewProvider {
    static var previews: some View {
        JiShiMapView()
    }
}



