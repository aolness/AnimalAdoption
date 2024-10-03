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
    // useIonViewWillEnter,
} from "@ionic/react";
import React from "react";
import { BASE } from "../constants";

const NewsList: React.FC = () => {
    // Declare a state variable to store the posts data
    const [posts, setPosts] = React.useState([]);

    // Define a function to fetch the posts data
    async function getNews() {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
        };

        const response = await fetch(`${BASE}/news/`, requestOptions);

        const data = await response.json();

        setPosts(data);
    }

    React.useEffect(() => {
        getNews();
    }, []);

    // useIonViewWillEnter(() => {
    //     console.log("ionViewWillEnter event fired");
    // });

    function createImg(post_animal) {
        if (post_animal && post_animal.image) {
            return (
                <IonCardContent>
                    <img width="100" height="100" src={post_animal.image} />
                </IonCardContent>
            );
        }

        return "";
    }

    return (
        <IonContent>
            {posts.map((post) => (
                <IonCard>
                    <IonCardHeader>
                        <IonCardTitle>{post.title}</IonCardTitle>
                        {/* <IonCardSubtitle></IonCardSubtitle> */}
                    </IonCardHeader>
                    {createImg(post.animal)}
                    
                    <IonCardContent>
                        <p>{post.author ? `By: ${post.author.username}` : ""}</p>
                        <p>{post.body}</p>
                    </IonCardContent>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default NewsList;
