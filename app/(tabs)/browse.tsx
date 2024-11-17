import { View, StyleSheet, Text } from "react-native";

export default function Browse() {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Browse</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
    },
});