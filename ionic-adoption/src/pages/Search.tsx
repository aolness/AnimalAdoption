import {
    // IonAvatar,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonContent,
    // IonHeader,
    // IonInfiniteScroll,
    // IonInfiniteScrollContent,
    // IonItem,
    // IonLabel,
    // IonList,
    // IonPage,
    // IonTitle,
    // IonToolbar,
} from "@ionic/react";
import React from "react";

const Search: React.FC = () => {
    return (
        <IonContent>
            <IonCard>
                <IonCardHeader>
                    <IonCardTitle>Search for cats</IonCardTitle>
                    <IonCardSubtitle>Placeholder cat search</IonCardSubtitle>
                </IonCardHeader>

                <IonCardContent>
                    <img
                        alt="Silhouette of mountains"
                        src="https://placekitten.com/100/103"
                    />
                </IonCardContent>
                <IonCardContent>A cat.</IonCardContent>
            </IonCard>
        </IonContent>
    );
};

export default Search;
