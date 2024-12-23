import { useEffect, useState} from 'react';
import {useRouter} from 'expo-router';
import { SafeAreaView, View, Text, Pressable, StyleSheet, Image } from 'react-native';
import Animated, { useSharedValue, withTiming, withSpring, useAnimatedStyle, runOnJS} from 'react-native-reanimated';
import { colours } from '@/util/colours';
import StartButton from './components/onboarding/StartButton';

export default function Index() {
  const router = useRouter();
  const opacity = useSharedValue(1);

  const logoImg = require('../assets/images/logo.png')
  return (
    <View style={{backgroundColor: colours.cream, flex: 1}}>
      <View style={styles.container}>
        <View style={styles.headingContainer}>
          <Image style={styles.logoImage} source={logoImg}/>
          <Text style={styles.heading}>SuChef</Text>
        </View>
        <View>
          <Text style={styles.subheading}>Meal planning, made simple</Text>
        </View>
        <View>
          <StartButton onPress={() => router.replace('/(tabs)')}/>
        </View>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  
  container: {
    marginTop: 50,
    marginHorizontal: 30,

  },
  headingContainer: {
    flexDirection: 'row',
    paddingRight: 10,
    alignItems: 'center',

  },
  logoImage: {
    width: 35,
    aspectRatio: 1,
    marginRight: 10,
  },
  heading: {
    fontFamily: 'Montserrat',
    fontSize: 35,
  },
  subheading: {
    marginTop: 50,
    marginHorizontal: 10,
    fontFamily: 'Hind-Bold',
    fontSize: 40,
    textAlign: 'center',
  },
  label: {
    color: colours.grey,
    
  }
})

