import { useEffect, useState} from 'react';
import {useRouter} from 'expo-router';
import { SafeAreaView, View, Text, Pressable, StyleSheet, Image } from 'react-native';
import Animated, { useSharedValue, withTiming, withSpring, useAnimatedStyle, runOnJS} from 'react-native-reanimated';


export default function Index() {
  const router = useRouter();
  const opacity = useSharedValue(1);

  const animatedStyle = useAnimatedStyle(() => ({
    opacity: opacity.value,
  }));
  const logoImg = require('./assets/images/logo.png')
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.headingContainer}>
        <Image style={styles.logoImage} source={logoImg}/>
        <Text style={styles.heading}>SuChef</Text>
        
      </View>
      <View>
        <Text style={styles.subheading}>Take back control of your food spending, without the compromise.</Text>
      </View>
      <Pressable 
          hitSlop={20} 
          onPress={() => router.replace("/(tabs)")}
          style={styles.startButtonContainer}
        >
          <Text style={styles.buttonLabel}>Get Started</Text>
        </Pressable>
    </SafeAreaView>
  );
}
const styles = StyleSheet.create({
  
  container: {
    flex: 1,
    marginTop: 80,
    marginHorizontal: 30,
  },
  headingContainer: {
    flexDirection: 'row',
    paddingRight: 10,
    alignItems: 'center'
  },
  logoImage: {
    width: 50,
    aspectRatio: 1,
    marginRight: 10,
  },
  heading: {
    fontFamily: 'Domine',
    fontSize: 50,
  },
  subheading: {
    marginTop: 20,
    fontFamily: 'Overpass',
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center'
  },
  startButtonContainer: {
    marginTop: 20,
    borderRadius: 5,
    borderColor: '#ccc',
    borderWidth: 1,
    width: '50%'
  },
  buttonLabel: {
    fontFamily: 'Overpass',
    fontSize: 16,
    padding: 5,
    textAlign: 'center'
  }
})

