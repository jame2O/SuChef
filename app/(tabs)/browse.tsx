import { View, StyleSheet, Text, TextInput, FlatList } from "react-native";
import { FontAwesome } from "@expo/vector-icons";
import RecipeCard from "../components/browse/RecipeCard";
import test_data from '../../api/data/test_data.json'
import { RecipeItem } from "../../util/Types";

let test_item: RecipeItem[] = test_data[0].data

export default function Browse() {
    return (
        <View style={styles.container}>
            <View style={styles.headingContainer}>
                <Text style={styles.title}>Browse Recipes</Text>
            </View>
            <View style={styles.searchBarContainer}>
                <FontAwesome size={22} name="search" />
                <TextInput 
                    placeholder="Search"
                    style={styles.searchBar}
                />
            </View>
            <View style={styles.cardsContainer}>
                <FlatList 
                    data={test_item}
                    scrollEnabled
                    numColumns={2}
                    renderItem={({item}) => 
                        <RecipeCard 
                            item={item} 
                            onPress={() => alert("Not yet implemented")}
                        />
                    }
                />
                
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignContent: 'flex-start',
        marginLeft: 20,
        marginRight: 20,
    },
    headingContainer: {
        marginTop: 60,
    },
    title: {
        fontSize: 40,
        fontFamily: 'Domine'
    },
    searchBarContainer: {
        flexDirection: 'row',
        marginTop: 20,
        borderWidth: 1,
        borderRadius: 10,
        padding: 10,
        borderColor: '#ccc',
        alignContent: 'center',
        alignItems: 'center',
        marginRight: 30
    },
    cardsWrapper: {
        justifyContent: 'space-between'
    },
    searchBar: {
        flex: 1,
        marginLeft: 10,
        fontSize: 18,
        fontFamily: 'Overpass',
    },
    cardsContainer: {
        marginTop: 20,
    }

});