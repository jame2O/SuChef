import { View, Text, StyleSheet, Pressable, Image, Dimensions } from "react-native";
import { RecipeItem } from '../../util/Types'
export default function RecipeCard({onPress, item}: {onPress: () => void, item: RecipeItem}) {
    const screenWidth = Dimensions.get('window').width;
    const cardWidth = (screenWidth / 2) - 40; // Adjust width to take up half the screen width minus padding
    return (
        <Pressable 
            onPress={onPress}>
            <View style={[styles.container, { width: cardWidth }]}>
                <Image
                    src={item.imageUrl}
                    style={styles.image}
                />
                <Text style={styles.label}>{item.name}</Text>
            </View>
        </Pressable>
    )
}

const styles = StyleSheet.create({
    container: {
        borderColor: '#1B1B1B',
        borderWidth: 1,
        borderRadius: 10,
        padding: 20,
        margin: 10,
        alignContent: 'center',
        alignItems: 'center'
    },
    image: {
        width: '100%',
        aspectRatio: 1,
        marginBottom: 5,
        borderRadius: 10,

    },
    label: {
        textAlign: 'center',
        fontSize: 16,
        fontFamily: 'Overpass',
        fontWeight: 'bold'
    }

})