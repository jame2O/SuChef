import { colours } from "@/util/colours";
import { View, Text, StyleSheet, SafeAreaView } from "react-native";
import LocationPicker from "../components/home/LocationPicker";
import * as Location from 'expo-location'
import { useState, useEffect } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function Index() {
    const [location, setLocation] = useState<Location.LocationObject | null>(null);
    const [address, setAddress] = useState<Location.LocationGeocodedAddress | null>(null);
    return (
        <SafeAreaView style={{backgroundColor: colours.cream, flex: 1}}>
            <View style={styles.container}>
                <View style={styles.top_bar}>
                    <LocationPicker location={location} setLocation={setLocation}/>
                    <Text style={styles.heading}>Welcome back!</Text>
                </View>
                <View style={styles.divider} />
            </View>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    container: {
        marginTop: 20,
        marginHorizontal: 20,
    },
    top_bar: {
        flexDirection: 'row',
        alignItems: 'center',
        padding: 5,
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        width: '100%'
    },
    heading: {
        fontFamily: 'Montserrat-Bold',
        alignContent: 'flex-end',
        textAlign: 'right',
        fontSize: 25
    },
    divider: {
        borderBottomColor: '#ccc',
        borderBottomWidth: 1,
        marginVertical: 10,
    },
    subheading: {
        fontFamily: 'Hind-Bold',
        textAlign: 'auto',
        fontSize: 30
    },
    label: {
        fontFamily: 'Hind',
        color: '#ccc',
        fontSize: 14
    }
})