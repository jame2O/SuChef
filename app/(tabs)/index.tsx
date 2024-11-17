import { Button, Pressable, Text, View, StyleSheet, ScrollView} from "react-native";
import { useState } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
export default function Index() {
  const link = "https://8703-92-236-107-198.ngrok-free.app"
  const [data, setData] = useState([])
  const [input, setInput] = useState('') 
  const getData = async (input: string) => {
    const response = await fetch(`${link}/scrape`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        item: `${input}`,
        stores: [2,1],
      }),
    }).catch((error) => {
      alert(error)
    })
    if (response) {
      const result = await response.json()
      setData(result)
    }
  }
  const getRecipes = async () => {
    const response = await fetch(`${link}/get_recipes`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    }).catch((error) => {
      alert(error)
    })
    if (response) {
      const result = await response.json()
      console.log(response)
      setData(result)
  }  
}
  return (
    <SafeAreaView
      style={styles.container}
    >
      <Text>Welcome!</Text>
      <Pressable onPress={() => getData("milk")}>
        <Text>Get Data</Text>
        
      </Pressable>
      <Pressable onPress={() => getRecipes()}>
        <Text>Get Recipes</Text>
        
      </Pressable>
      <ScrollView>
            <Text style={styles.text}>Items</Text>
            {data.map((item: any, index: number) => (
              <View key={index}>
                <Text>{item.Brand}</Text>
                <Text>{item.Description}</Text>
                <Text>{item.ListPrice}</Text>
                <Text>{item.UnitPrice}</Text>
              </View>
            ))}
      </ScrollView>
    </SafeAreaView>
  );
}


const styles = StyleSheet.create({
 container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontFamily: 'Overpass',
    fontSize: 50,
  }
})
