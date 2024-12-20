import { SplashScreen, Stack, Tabs } from "expo-router";
import { useFonts } from "expo-font";
import { useEffect } from "react";

SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [fontsLoaded, fontsError] = useFonts({
    'Overpass': require('../assets/fonts/Overpass.ttf'),
    'Overpass-Italic': require('../assets/fonts/Overpass-Italic.ttf'),
    'Domine': require('../assets/fonts/Domine.ttf'),
    'Montserrat': require('../assets/fonts/Montserrat/Montserrat-Medium.ttf'),
    'Montserrat-Bold': require('../assets/fonts/Montserrat/Montserrat-Bold.ttf'),
    'Montserrat-Italic': require('../assets/fonts/Montserrat/Montserrat-MediumItalic.ttf'),
    'Hind': require('../assets/fonts/Hind/Hind-Regular.ttf'),
    'Hind-Bold': require('../assets/fonts/Hind/Hind-Bold.ttf'),
  })
  useEffect(() => {
    async function prepareApp() {
      if (fontsLoaded) {
        console.log('Fonts loaded');
        await SplashScreen.hideAsync();
      }
    }
    prepareApp();
  }, [fontsLoaded, fontsError]);

  return (
    <Stack>
      <Stack.Screen name="index" options={{headerShown: false}}/>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
    </Stack>
  );
}
