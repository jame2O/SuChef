import { useEffect, useState} from 'react';
import {useRouter} from 'expo-router';
import { SafeAreaView, View, Text, Pressable, StyleSheet } from 'react-native';
import Animated, { useSharedValue, withTiming, withSpring, useAnimatedStyle, runOnJS} from 'react-native-reanimated';

export default function Index() {
  const router = useRouter();
  const words = ["work", "workouts", "sports night", "uni life", "socials"]
  const opacity = useSharedValue(1);
  const [word, setWord] = useState("life");

  const animatedStyle = useAnimatedStyle(() => ({
    opacity: opacity.value,
  }));

  return (
    <SafeAreaView style={styles.container}>
      <View style={[styles.splashContainer]}>
        <Text style={styles.text}>SuChef is a meal planner which works around you.</Text>
        <Text>Set a budget, browse recipes, and let SuChef do the rest.</Text>
        <Pressable hitSlop={20} onPress={() => router.replace("/(tabs)")}>
          <Text>Get Started</Text>
        </Pressable>
      </View>
    </SafeAreaView>
  );
  
}
const styles = StyleSheet.create({
  
  container: {
    flex: 1,
    padding: 30,
    alignContent: "center",
    alignItems: "center",
  },
  splashContainer: {
    borderRadius: 10,
    padding: 10,
  },
  text: {
    fontFamily: 'Domine',
    fontSize: 50,
  },
})

