import {
    IonButton,
    IonCard,
    IonCardContent,
    IonContent,
    IonFooter,
    IonHeader,
    IonInput,
    IonPage,
    IonTitle,
    IonToolbar,
    useIonRouter,
    useIonAlert,
} from "@ionic/react";
import React from "react";
import { BASE } from "../constants";

const Register: React.FC = () => {
    const router = useIonRouter();
    const [user, setUser] = React.useState("");
    const [email, setEmail] = React.useState("");
    const [password, setPass] = React.useState("");
    const [presentAlert] = useIonAlert();

    const doRegister = async () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: user,
                email: email,
                password: password,
            }),
        };

        const response = await fetch(`${BASE}/register/`, requestOptions);
        
        if (response.ok) {
            router.push("/");
        }
        else {
            const data = await response.json();

            if(!data) {
                presentAlert({
                    header: "Error",
                    subHeader: "",
                    message: "Unknown error.",
                    buttons: ["OK"],
                });
            }
            else {
                if(data.email) {
                    presentAlert({
                        header: "Error",
                        subHeader: "",
                        message: "Please enter a valid email address.",
                        buttons: ["OK"],
                    });
                }
                else if(data.username) {
                    presentAlert({
                        header: "Error",
                        subHeader: "",
                        message: "Username is either invalid or already taken.",
                        buttons: ["OK"],
                    });
                }
            }
        }
    };

    return (
        <IonPage>
            <IonHeader>
                <IonToolbar>
                    <IonTitle>Pawfect Matchmaker</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <IonCard>
                    <IonCardContent>
                        <IonInput
                            label="Username"
                            type="text"
                            fill="outline"
                            placeholder="doglover99"
                            labelPlacement="floating"
                            onIonChange={(e) => setUser(e.detail.value)}
                        ></IonInput>
                        <IonInput
                            className="ion-margin-top"
                            label="Email"
                            type="email"
                            fill="outline"
                            placeholder="doglover99@example.com"
                            labelPlacement="floating"
                            onIonChange={(e) => setEmail(e.detail.value)}
                        ></IonInput>
                        <IonInput
                            className="ion-margin-top"
                            label="Password"
                            type="password"
                            fill="outline"
                            labelPlacement="floating"
                            onIonChange={(e) => setPass(e.detail.value)}
                        ></IonInput>
                        <IonButton
                            className="ion-margin-top"
                            type="submit"
                            expand="block"
                            onClick={doRegister}
                        >
                            Create New Account
                        </IonButton>
                    </IonCardContent>
                </IonCard>
            </IonContent>
        </IonPage>
    );
};

export default Register;
