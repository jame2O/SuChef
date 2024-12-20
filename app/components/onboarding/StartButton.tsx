import { Pressable, View, Text, StyleSheet } from "react-native";
import { colours } from "@/util/colours";
export default function StartButton({onPress}: {onPress: () => void}) {
    return (
        <Pressable style={styles.buttonContainer}>
            <Text style={styles.label}>Get Started</Text>
        </Pressable>
    )
}
const styles = StyleSheet.create({
    buttonContainer: {
        flexDirection: 'row',
        backgroundColor: colours.dark_brown,
        borderRadius: 20,
        justifyContent: 'center',
        padding: 5,

    },
    label: {
        color: colours.white,
        fontSize: 20,
        fontFamily: 'Hind-Bold'
    }
})