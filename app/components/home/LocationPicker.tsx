import { View, StyleSheet, Pressable, Text } from "react-native";
import { FontAwesome } from "@expo/vector-icons";
import * as Location from 'expo-location'
import { useState, useEffect } from "react";
import { colours } from "@/util/colours";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function LocationPicker({location, setLocation}: {location: Location.LocationObject | null, setLocation: () => void}) {    const [address, setAddress] = useState<Location.LocationGeocodedAddress | null>(null)
    const storeData = async (key:string, value: string) => {
        try {
          await AsyncStorage.setItem(key, value);
        } catch (e) {
          console.error("unable to save data to storage")
        }
      };
    const getLocation = async () => {
        let {status} = await Location.requestForegroundPermissionsAsync();
        // If we get location perms, go ahead
        if (status === 'granted') {
            console.log("Location permissions granted");
        } else {
            console.error("Locations permissions denied")
            return;
        }

        let loc = await Location.getCurrentPositionAsync({});
        if (!loc) {
            console.error("Unable to fetch location")
            return;
        }
        setLocation(loc)
        // stringify coords ready for storage
        const locStr = JSON.stringify({
            lat: loc.coords.latitude,
            lng: loc.coords.longitude
        })
        storeData("location", locStr)
        return;
    }
    return (
        <View style={styles.container}>
            <Pressable onPress={getLocation}>
                <FontAwesome name="location-arrow" size={30} color="grey"/>
            </Pressable>
            <Text style={styles.label}>Location: {address !== null ? `${address.city}, ${address.country}` : "N/A"}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        padding: 5,
        alignItems: 'center',
        flexDirection: 'row',
    },
    label: {
        fontFamily: 'Hind',
        paddingLeft: 10,
        fontSize: 16,
        color: 'grey',
    }
})