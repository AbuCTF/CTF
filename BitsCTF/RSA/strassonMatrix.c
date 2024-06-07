#include <stdio.h>

void matrixA_DAC(int a[4][4], int p[2][2], int q[2][2], int r[2][2], int s[2][2]) {
    // Top-left  2x2 matrix
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            p[i][j] = a[i][j];
        }
    }

    // Top-right  2x2 matrix
    for (int i =  0; i <  2; i++) {
        for (int j =  2; j <  4; j++) {
            q[i][j-2] = a[i][j];
        }
    }

    // Bottom-left  2x2 matrix
    for (int i =  2; i <  4; i++) {
        for (int j =  0; j <  2; j++) {
            r[i-2][j] = a[i][j];
        }
    }

    // Bottom-right  2x2 matrix
    for (int i =  2; i <  4; i++) {
        for (int j =  2; j <  4; j++) {
            s[i-2][j-2] = a[i][j];
        }
    }
}

void matrixB_DAC(int b[4][4], int l[2][2], int m[2][2], int n[2][2], int o[2][2]) {
    // Top-left  2x2 matrix
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            l[i][j] = b[i][j];
        }
    }

    // Top-right  2x2 matrix
    for (int i =  0; i <  2; i++) {
        for (int j =  2; j <  4; j++) {
            m[i][j-2] = b[i][j];
        }
    }

    // Bottom-left  2x2 matrix
    for (int i =  2; i <  4; i++) {
        for (int j =  0; j <  2; j++) {
            n[i-2][j] = b[i][j];
        }
    }

    // Bottom-right  2x2 matrix
    for (int i =  2; i <  4; i++) {
        for (int j =  2; j <  4; j++) {
            o[i-2][j-2] = b[i][j];
        }
    }
}


// Function to multiply two matrices

/* void multiplyMatrices(int a[4][4], int b[4][4], int result[4][4]) {
    for (int i =  0; i <  4; i++) {
        for (int j =  0; j <  4; j++) {
            result[i][j] =  0;
            for (int k =  0; k <  4; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
} */


int main(){
    int a[4][4], b[4][4], result[4][4], i, j;
    int p[2][2], q[2][2], r[2][2], s[2][2];
    int l[2][2], m[2][2], n[2][2], o[2][2];
    int P1, Q1, R1, S1, T1, U1, V1;
    int P2, Q2, R2, S2, T2, U2, V2;
    int P3, Q3, R3, S3, T3, U3, V3;
    int P4, Q4, R4, S4, T4, U4, V4;
    int P5, Q5, R5, S5, T5, U5, V5;
    int P6, Q6, R6, S6, T6, U6, V6;
    int P7, Q7, R7, S7, T7, U7, V7;
    int P8, Q8, R8, S8, T8, U8, V8;
    int C1[2][2], C2[2][2];
    int D1[2][2], D2[2][2];
    int E1[2][2], E2[2][2];
    int F1[2][2], F2[2][2];
    int resultC[2][2], resultD[2][2], resultE[2][2], resultF[2][2];
    int finalResult[4][4];

    printf("Enter the 16 values for first 4/4 Matrix:");
    for(i = 0;i < 4; i++)
        for(j = 0;j < 4;j++)
            scanf("%d", &a[i][j]);

    printf("Enter the 16 values for second 4/4 Matrix:");
    for(i = 0;i < 4; i++)
        for(j = 0;j < 4;j++)
            scanf("%d", &b[i][j]);

    printf("\nThe first matrix is:\n");
    for(i = 0;i < 4; i++){
        printf("\n");
        for(j = 0;j < 4; j++)
            printf("%d\t", a[i][j]);
    }

    printf("\nThe second matrix is:\n");
    for(i = 0;i < 4; i++){
        printf("\n");
        for(j = 0;j < 4; j++)
            printf("%d\t", b[i][j]);
    }

    printf("\n***********************\n");
    printf("Splitting matrix A into 4 sub-matrices:\n");

    // DAC performed on the matrix A
    matrixA_DAC(a, p, q, r, s);

    // Print the  2x2 matrices
    printf("Top-left  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", p[i][j]);
        }
        printf("\n");
    }

    printf("Top-right  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", q[i][j]);
        }
        printf("\n");
    }

    printf("Bottom-left  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", r[i][j]);
        }
        printf("\n");
    }

    printf("Bottom-right  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", s[i][j]);
        }
        printf("\n");
    }

    printf("\n***********************\n");
    printf("Splitting matrix A into 4 sub-matrices:\n");

    // DAC performed on the matrix B
    matrixB_DAC(b, l, m, n, o);

    // Print the  2x2 matrices
    printf("Top-left  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", l[i][j]);
        }
        printf("\n");
    }

    printf("Top-right  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }

    printf("Bottom-left  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", n[i][j]);
        }
        printf("\n");
    }

    printf("Bottom-right  2x2 matrix:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", o[i][j]);
        }
        printf("\n");
    }

    printf("\nApplying Strasson's Matrix Multiplication Algorithm:\n");
    printf("\nTop-left section of the 4/4 matrix:\n");
    P1 = ((p[0][0] + p[1][1]) * (l[0][0] + l[1][1]));
    Q1 = ((p[1][0] + p[1][1]) * l[0][0]);
    R1 = (p[0][0] * (q[0][1] - l[1][1]));
    S1 = (p[1][1] * (q[1][0] - l[0][0]));
    T1 = ((p[0][1] + p[0][1]) * l[1][1]);
    U1 = ((p[1][0] - p[0][0]) * (l[0][0] + l[1][1]));
    V1 = ((p[0][1] - p[1][1]) * (l[1][0] + l[1][1]));


    C1[0][0] = P1 + S1 - T1 + V1;
    C1[0][1] = R1 + T1;
    C1[1][0] = Q1 + S1;
    C1[1][1] = P1 + R1 - Q1 + U1;

    printf("\nMatrixA:\n");
    for (int i =  0; i <  2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", C1[i][j]);
        }
        printf("\n");
    }

    P2 = ((q[0][0] + q[1][1]) * (n[0][0] + n[1][1]));
    Q2 = ((q[1][0] + q[1][1]) * n[0][0]);
    R2 = (q[0][0] * (q[0][1] - n[1][1]));
    S2 = (q[1][1] * (q[1][0] - n[0][0]));
    T2 = ((q[0][1] + q[0][1]) * n[1][1]);
    U2 = ((q[1][0] - q[0][0]) * (n[0][0] + n[1][1]));
    V2 = ((q[0][1] - q[1][1]) * (n[1][0] + n[1][1]));

    C2[0][0] = P2 + S2 - T2 + V2; 
    C2[0][1] = R2 + T2;           
    C2[1][0] = Q2 + S2;          
    C2[1][1] = P2 + R2 - Q2 + U2; 


    printf("\nMatrixB:\n");
    for (int i =   0; i <   2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", C2[i][j]);
        }
        printf("\n");
    }

    // Add C1 and C2 matrices
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            resultC[i][j] = C1[i][j] + C2[i][j];
        }
    }

    // Print the resultC matrix
    printf("\nThe resultC matrix after adding C1 and C2:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", resultC[i][j]);
        }
        printf("\n");
    }


    printf("\nTop-right section of the 4/4 matrix:\n");
    P3 = ((p[0][0] + p[1][1]) * (m[0][0] + m[1][1]));
    Q3 = ((p[1][0] + p[1][1]) * m[0][0]);
    R3 = (p[0][0] * (q[0][1] - m[1][1]));
    S3 = (p[1][1] * (q[1][0] - m[0][0]));
    T3 = ((p[0][1] + p[0][1]) * m[1][1]);
    U3 = ((p[1][0] - p[0][0]) * (m[0][0] + m[1][1]));
    V3 = ((p[0][1] - p[1][1]) * (m[1][0] + m[1][1]));


    D1[0][0] = P3 + S3 - T3 + V3;
    D1[0][1] = R3 + T3;
    D1[1][0] = Q3 + S3;
    D1[1][1] = P3 + R3 - Q3 + U3;

    printf("\nMatrixA:\n");
    for (int i =  0; i <  2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", D1[i][j]);
        }
        printf("\n");
    }

    P4 = ((q[0][0] + q[1][1]) * (o[0][0] + o[1][1]));
    Q4 = ((q[1][0] + q[1][1]) * o[0][0]);
    R4 = (q[0][0] * (q[0][1] - o[1][1]));
    S4 = (q[1][1] * (q[1][0] - o[0][0]));
    T4 = ((q[0][1] + q[0][1]) * o[1][1]);
    U4 = ((q[1][0] - q[0][0]) * (o[0][0] + o[1][1]));
    V4 = ((q[0][1] - q[1][1]) * (o[1][0] + o[1][1]));

    D2[0][0] = P4 + S4 - T4 + V4; 
    D2[0][1] = R4 + T4;           
    D2[1][0] = Q4 + S4;          
    D2[1][1] = P4 + R4 - Q4 + U4; 

    printf("\nMatrixB:\n");
    for (int i =   0; i <   2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", D2[i][j]);
        }
        printf("\n");
    }

    // Add D1 and D2 matrices
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            resultD[i][j] = D1[i][j] + D2[i][j];
        }
    }

    // Print the resultD matrix
    printf("\nThe resultD matrix after adding D1 and D2:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", resultD[i][j]);
        }
        printf("\n");
    }


    printf("\nBottom-left section of the 4/4 matrix:\n");
    P5 = ((r[0][0] + r[1][1]) * (l[0][0] + l[1][1]));
    Q5 = ((r[1][0] + r[1][1]) * l[0][0]);
    R5 = (r[0][0] * (q[0][1] - l[1][1]));
    S5 = (r[1][1] * (q[1][0] - l[0][0]));
    T5 = ((r[0][1] + r[0][1]) * l[1][1]);
    U5 = ((r[1][0] - r[0][0]) * (l[0][0] + l[1][1]));
    V5 = ((r[0][1] - r[1][1]) * (l[1][0] + l[1][1]));
    E1[0][0] = P5 + S5 - T5 + V5;
    E1[0][1] = R5 + T5;
    E1[1][0] = Q5 + S5;
    E1[1][1] = P5 + R5 - Q5 + U5;

    printf("\nMatrixA:\n");
    for (int i =  0; i <  2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", E1[i][j]);
        }
        printf("\n");
    }

    P6 = ((s[0][0] + s[1][1]) * (n[0][0] + n[1][1]));
    Q6 = ((s[1][0] + s[1][1]) * n[0][0]);
    R6 = (s[0][0] * (s[0][1] - n[1][1]));
    S6 = (s[1][1] * (s[1][0] - n[0][0]));
    T6 = ((s[0][1] + s[0][1]) * n[1][1]);
    U6 = ((s[1][0] - s[0][0]) * (n[0][0] + n[1][1]));
    V6 = ((s[0][1] - s[1][1]) * (n[1][0] + n[1][1]));

    E2[0][0] = P6 + S6 - T6 + V6;
    E2[0][1] = R6 + T6;
    E2[1][0] = Q6 + S6;
    E2[1][1] = P6 + R6 - Q6 + U6;

    printf("\nMatrixB:\n");
    for (int i =   0; i <   2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", E2[i][j]);
        }
        printf("\n");
    }

    // Add E1 and E2 matrices
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            resultE[i][j] = E1[i][j] + E2[i][j];
        }
    }

    // Print the resultE matrix
    printf("\nThe resultE matrix after adding E1 and E2:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", resultE[i][j]);
        }
        printf("\n");
    }


    printf("\nBottom-right section of the 4/4 matrix:\n");
    P7 = ((r[0][0] + r[1][1]) * (m[0][0] + m[1][1]));
    Q7 = ((r[1][0] + r[1][1]) * m[0][0]);
    R7 = (r[0][0] * (q[0][1] - m[1][1]));
    S7 = (r[1][1] * (q[1][0] - m[0][0]));
    T7 = ((r[0][1] + r[0][1]) * m[1][1]);
    U7 = ((r[1][0] - r[0][0]) * (m[0][0] + m[1][1]));
    V7 = ((r[0][1] - r[1][1]) * (m[1][0] + m[1][1]));

    F1[0][0] = P7 + S7 - T7 + V7;
    F1[0][1] = R7 + T7;
    F1[1][0] = Q7 + S7;
    F1[1][1] = P7 + R7 - Q7 + U7;

    printf("\nMatrixA:\n");
    for (int i =  0; i <  2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", F1[i][j]);
        }
        printf("\n");
    }

    P8 = ((s[0][0] + s[1][1]) * (o[0][0] + o[1][1]));
    Q8 = ((s[1][0] + s[1][1]) * o[0][0]);
    R8 = (s[0][0] * (s[0][1] - o[1][1]));
    S8 = (s[1][1] * (s[1][0] - o[0][0]));
    T8 = ((s[0][1] + s[0][1]) * o[1][1]);
    U8 = ((s[1][0] - s[0][0]) * (o[0][0] + o[1][1]));
    V8 = ((s[0][1] - s[1][1]) * (o[1][0] + o[1][1]));

    F2[0][0] = P8 + S8 - T8 + V8;
    F2[0][1] = R8 + T8;
    F2[1][0] = Q8 + S8;
    F2[1][1] = P8 + R8 - Q8 + U8;

    printf("\nMatrixB:\n");
    for (int i =   0; i <   2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", F2[i][j]);
        }
        printf("\n");
    }

    // Add F1 and F2 matrices
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            resultF[i][j] = F1[i][j] + F2[i][j];
        }
    }

    // Print the resultF matrix
    printf("\nThe resultF matrix after adding F1 and F2:\n");
    for (int i =  0; i <  2; i++) {
        for (int j =  0; j <  2; j++) {
            printf("%d ", resultF[i][j]);
        }
        printf("\n");
    }

    // Assign elements from resultC to the top-left  2x2 matrix of finalResult
    finalResult[0][0] = resultC[0][0];
    finalResult[0][1] = resultC[0][1];
    finalResult[1][0] = resultC[1][0];
    finalResult[1][1] = resultC[1][1];

    // Assign elements from resultD to the top-right  2x2 matrix of finalResult
    finalResult[0][2] = resultD[0][0];
    finalResult[0][3] = resultD[0][1];
    finalResult[1][2] = resultD[1][0];
    finalResult[1][3] = resultD[1][1];

    // Assign elements from resultE to the bottom-left  2x2 matrix of finalResult
    finalResult[2][0] = resultE[0][0];
    finalResult[2][1] = resultE[0][1];
    finalResult[3][0] = resultE[1][0];
    finalResult[3][1] = resultE[1][1];

    // Assign elements from resultF to the bottom-right  2x2 matrix of finalResult
    finalResult[2][2] = resultF[0][0];
    finalResult[2][3] = resultF[0][1];
    finalResult[3][2] = resultF[1][0];
    finalResult[3][3] = resultF[1][1];

    
    // Print the finalResult matrix
    printf("\n************************************\n");
    printf("\nThe finalResult matrix:\n");
    for (int i =  0; i <  4; i++) {
        for (int j =  0; j <  4; j++) {
            printf("%d ", finalResult[i][j]);
        }
        printf("\n");
    }

    return  0;


    /* multiplyMatrices(a, b, result);

    printf("\nThe resultant matrix after strasson's algorithm:\n");
    for (int i =  0; i <  4; i++) {
        for (int j =  0; j <  4; j++) {
            printf("%d\t", result[i][j]);
        }
        printf("\n");
    } */

}