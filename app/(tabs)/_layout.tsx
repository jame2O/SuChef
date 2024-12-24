import { Tabs } from "expo-router";
import { FontAwesome, FontAwesome5 } from "@expo/vector-icons";
import { colours } from "@/util/colours";
export default function TabsLayout() {
    return (
        <Tabs screenOptions={{
            headerShown: false,
            tabBarLabelStyle: {
                fontSize: 12,
                fontFamily: 'Hind'
            },
            tabBarActiveTintColor: colours.dark_brown
            }}>
            <Tabs.Screen
                name="index"
                options={{
                    title: 'Home',
                    tabBarIcon: ({ color }) => <FontAwesome size={26} name="home" color={color} />,
                    headerShown: false,
                }}
            />
            <Tabs.Screen
                name="browse"
                options={{
                    title: 'Discover',
                    tabBarIcon: ({ color }) => <FontAwesome size={26} name="compass" color={color} />,
                    headerShown: false,
                }}
            />
            <Tabs.Screen
                name="shopping-list"
                options={{
                    title: 'Shopping List',
                    tabBarIcon: ({ color }) => <FontAwesome size={26} name="shopping-cart" color={color} />,
                    headerShown: false,
                }}
            />
            <Tabs.Screen
                name="profile"
                options={{
                    title: 'Profile',
                    tabBarIcon: ({ color }) => <FontAwesome5 size={26} name="user-alt" color={color} />,
                    headerShown: false,
                }}
            />

        </Tabs>
    )
}