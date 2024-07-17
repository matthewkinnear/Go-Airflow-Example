package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type DagRunRequest struct {
	Conf string `json:"conf"`
}

func triggerDag(dagId string) error {
	url := fmt.Sprintf("http://airflow-webserver:8080/api/v1/dags/%s/dagRuns", dagId)

	dagRunRequest := DagRunRequest{
		Conf: "{}",
	}
	reqBody, err := json.Marshal(dagRunRequest)
	if err != nil {
		return fmt.Errorf("failed to marshal request body: %w", err)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(reqBody))
	if err != nil {
		return fmt.Errorf("failed to create request: %w", err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.SetBasicAuth("airflow", "airflow")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return fmt.Errorf("failed to send request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		fmt.Println("DAG triggered successfully")
	} else {
		fmt.Printf("Failed to trigger DAG: %s\n", resp.Status)
	}

	return nil
}

func main() {
	dagId := "fetch_random_person_dag"
	if len(os.Args) > 1 {
		dagId = os.Args[1]
	}

	err := triggerDag(dagId)
	if err != nil {
		fmt.Printf("Error: %s\n", err)
		os.Exit(1)
	}
}
