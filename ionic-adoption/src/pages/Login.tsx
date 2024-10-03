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

const Login: React.FC = () => {
    const router = useIonRouter();
    const [user, setUser] = React.useState("");
    const [password, setPass] = React.useState("");
    const [presentAlert] = useIonAlert();

    const doLogin = async () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: user, password: password }),
        };

        const response = await fetch(`${BASE}/login/`, requestOptions);
        if (response.ok) {
            const data = await response.json();
            const token = data.access;

            // TODO: Long term I might not want to store in localStorage.
            localStorage.setItem("token", token);
            // Options prevent the user from going back:
            router.push("/app", "root", "replace");
        }
        else {
            console.log("Invalid username or password");
            presentAlert({
                header: "Error",
                subHeader: "",
                message: "Invalid username or password",
                buttons: ["OK"],
            });
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
                            onClick={doLogin}
                        >
                            Login
                        </IonButton>
                        <IonButton
                            className="ion-margin-top"
                            type="button"
                            expand="block"
                            routerLink="/register"
                        >
                            New Account
                        </IonButton>
                    </IonCardContent>
                </IonCard>
            </IonContent>
            {/* <IonFooter>
                <IonToolbar className="ion-padding">Blah blah footer</IonToolbar>
            </IonFooter> */}
        </IonPage>
    );
};

export default Login;
