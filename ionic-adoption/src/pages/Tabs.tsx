import {
    // IonContent,
    // IonHeader,
    IonIcon,
    IonLabel,
    // IonPage,
    IonRouterOutlet,
    IonTabBar,
    IonTabButton,
    IonTabs,
    // IonTitle,
    // IonToolbar,
} from "@ionic/react";
import React from "react";
import NewsList from "./NewsList";
import Search from "./Search";
import { Redirect, Route } from "react-router-dom";
import { search, newspaperOutline } from "ionicons/icons";


const Tabs: React.FC = () => {
    return (
        <IonTabs>
            <IonRouterOutlet>
                <Route path="/app/news">
                    <NewsList />
                </Route>
                <Route path="/app/search">
                    <Search />
                </Route>
                <Route exact path="/app">
                    <Redirect to="/app/news" />
                </Route>
            </IonRouterOutlet>
            <IonTabBar slot="bottom">
                <IonTabButton tab="radio" href="/app/news">
                    <IonIcon icon={newspaperOutline} />
                    <IonLabel>News</IonLabel>
                </IonTabButton>

                <IonTabButton tab="search" href="/app/search">
                    <IonIcon icon={search} />
                    <IonLabel>Search</IonLabel>
                </IonTabButton>
            </IonTabBar>
        </IonTabs>
    );
};

export default Tabs;

// import Register from './pages/Register';

//         <Route component={ Register } path="/register" exact />
